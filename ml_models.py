import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
import joblib


class Models:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, Y, test_size=0.2, random_state=316)
        self.score = None

    def run_model(self, regressor, name):
        regressor.fit(self.X_train, self.y_train)
        self.score = regressor.score(self.X_test, self.y_test)
        predicted = regressor.predict(self.X)
        df = pd.DataFrame(predicted, columns=[
            'height', 'width', 'penetration'])
        df.to_excel(f'model/data/{name}.xlsx', index=False)
        joblib.dump(regressor, f'model/saved/model_{name}.pkl')
        return regressor

    def linear_regression(self):
        regressor = LinearRegression()
        return self.run_model(regressor, name='linear_regression')

    def ploynomial_regression(self):
        poly = PolynomialFeatures(degree=3)
        X_poly = poly.fit_transform(self.X_train)
        poly.fit(X_poly, self.y_train)
        regressor = LinearRegression()
        regressor.fit(X_poly, self.y_train)
        self.score = regressor.score(
            poly.fit_transform(self.X_test), self.y_test)
        predicted = regressor.predict(poly.fit_transform(self.X))
        df_poly = pd.DataFrame(predicted, columns=[
                               'height', 'width', 'penetration'])
        df_poly.to_excel('model/data/polynomial_regression.xlsx', index=False)
        joblib.dump(regressor, f'model/saved/model_polynomial_regression.pkl')
        return regressor

    def decision_tree(self):
        regressor = DecisionTreeRegressor(random_state=0)
        return self.run_model(regressor, name='decision_tree_regression')

    def random_forest(self):
        regressor = RandomForestRegressor(
            n_estimators=10, random_state=0)
        return self.run_model(regressor, name='random_forest_regression')

    def lasso_regression(self):
        regressor = Lasso(alpha=1.0)
        return self.run_model(regressor, name='lasso_regression')

    def ridge_regression(self):
        regressor = Ridge(alpha=1.0)
        return self.run_model(regressor, name='ridge_regression')
