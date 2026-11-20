# workflow>x

## 节点类型

`workflow>x`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `提示词1:STRING`（1 次）
- `提示词2:STRING`（1 次）
- `If there is a person/character in the image you must refer to them as {name}.:BOOLEAN`（1 次）
- `Do NOT include information about people/characters that cannot be changed (like ethnicity, gender, etc), but do still include changeable attributes (like hair style).:BOOLEAN`（1 次）
- `Include information on the image's composition style, such as leading lines, rule of thirds, or symmetry.:BOOLEAN`（1 次）
- `Do NOT mention any text that is in the image.:BOOLEAN`（1 次）
- `Specify the depth of field and whether the background is in focus or blurred.:BOOLEAN`（1 次）
- `If applicable, mention the likely use of artificial or natural lighting sources.:BOOLEAN`（1 次）
- `Do NOT use any ambiguous language.:BOOLEAN`（1 次）

## 输出

- `条件:CONDITIONING`（1 次）
- `FluxGuidance 条件:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, false, false, true, false, true, false, false, false, false, false, false, false, false, true, true, true, "unsl`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
