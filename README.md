# final-year-project

<div>
    <p>
        With this piece of software, we are trying to predict Height, Width and Penetration of
        a Weld Bead using Arc Voltage, Current, Travel Speed and Nozzle to Plate Distance as
        our input.
    </p>
    <table class="table">
        <thead>
        <tr>
            <th scope="col">Parameters</th>
            <th scope="col">Represents</th>
            <th scope="col">range</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>V</td>
            <td>Arc Voltage</td>
            <td>22 - 36 V</td>
        </tr>
        <tr>
            <td>A</td>
            <td>Current</td>
            <td>250 - 550 A</td>
        </tr>
        <tr>
            <td>S</td>
            <td>Travel Speed</td>
            <td>6 - 18 mm/sec</td>
        </tr>
        <tr>
            <td>N</td>
            <td>Nozzle to Plate Distance</td>
            <td>20 - 34 mm</td>
        </tr>
        </tbody>
    </table>
    <p>All the outputs (Bead Height, Width and Penetration) are measured in mm.</p>
    <h3>Weld Bead Geometry</h3>
    <!-- Weld Bead svg -->
    <svg viewBox="0 0 100 50" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <marker
            id="arrow"
            viewBox="0 0 10 10"
            refX="10"
            refY="5"
            markerWidth="6"
            markerHeight="6"
            orient="auto-start-reverse"
            >
            <path d="M 0 0 L 10 5 L 0 10 z" />
            </marker>
        </defs>
        <!-- Weld Bead Cross Section -->
        <path
            fill="#94a1a8"
            d="
            M10,10
            C15,0,45,0,50,10
            Q30,60,10,10
            "
        ></path>
        <!-- Arrows -->
        <path d="M10,12 L10,40" stroke="black" stroke-width="0.2"></path>
        <path d="M50,12 L50,40" stroke="black" stroke-width="0.2"></path>
        <path
            d="M10,40 L50,40"
            marker-start="url(#arrow)"
            marker-end="url(#arrow)"
            stroke="black"
            stroke-width="0.2"
        ></path>
        <path d="M52,10 L62,10" stroke="black" stroke-width="0.2"></path>
        <path d="M32,35 L62,35" stroke="black" stroke-width="0.2"></path>
        <path
            d="M62,10 L62,35"
            marker-start="url(#arrow)"
            marker-end="url(#arrow)"
            stroke="black"
            stroke-width="0.2"
        ></path>
        <path d="M32,2.5 L62,2.5" stroke="black" stroke-width="0.2"></path>
        <path
            d="M62,2.5 L62,10"
            marker-start="url(#arrow)"
            marker-end="url(#arrow)"
            stroke="black"
            stroke-width="0.2"
        ></path>
        <!-- Measurements Text -->
        <text x="63" y="6.75" fill="black" font-size="2.5">Height</text>
        <text x="28" y="43" fill="black" font-size="2.5">Width</text>
        <text x="63" y="22" fill="black" font-size="2.5">Penetration</text>
    </svg>
</div>
