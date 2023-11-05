#version 330 core

layout (location = 0) out vec4 fragColor;

const vec3 gamma = vec3(2.2);
const vec3 inv_gamma = 1 / gamma;

uniform sampler2D u_texture_0;

in vec3 voxel_color;
in vec2 uv;
in float shading;

void main() {
    vec3 tex_col = texture(u_texture_0, uv).rgb;
    tex_col = pow(tex_col, gamma);

    tex_col.rgb *= voxel_color;
    tex_col *= shading;

    tex_col = pow(tex_col, inv_gamma);
    fragColor = vec4(tex_col, 1);
}
