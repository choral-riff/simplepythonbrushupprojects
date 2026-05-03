class Particle:
    #constructor function 
    #defines the state of the particle 
    def __init__(self, mass, position, velocity):
        print(f"Creating a particle with mass {mass} kg, position {position}m on 1D axis, velocity {velocity} m/s")
        self.mass = mass
        self.position = position
        self.velocity = velocity

    #dt = delta time
    def update_position(self, dt):
        print(f"\n Calculating the change in the position of the particle in time {dt}: \n")
        d_position = self.velocity*dt
        updated_position = self.position + d_position
        self.position = updated_position
        print(f" The updated position of the particle is {updated_position}m" )

    #allow force to affect velocity of the particle 
    def apply_force(self, force, dt):
        print("\n Force will produce an acceleration on the particle. \n")
        print(f" The force {force}N applied on the particle over a time {dt}sec produces an acceleration as follows: \n")
        acceleration = force/self.mass
        print(f"Acceleration produced = {force}/{self.mass} = {acceleration}")
        final_v = self.velocity + (acceleration*dt)
        print(f"The new velocity due to application of force over {dt}sec is {final_v}")
        self.velocity = final_v

#creates a particle with mass 2 kg, pos 0.0m, velocity 0.0m/s
firstParticle = Particle(2.0, 0.0, 0.0)
#applying a force of 10N over a time of 1.0sec on the particle 
firstParticle.apply_force(10, 1.0)
#since the force applied over dt changes the velocity and position, we need to change the position too 
firstParticle.update_position(1.0)





