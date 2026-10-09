# OllamaCaptionerExtraOptions

## 节点类型

`OllamaCaptionerExtraOptions`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `If there is a person/character in the image you must refer to them as {name}.:BOOLEAN`（1 次）
- `Do NOT include information about people/characters that cannot be changed (like ethnicity, gender, etc), but do still include changeable attributes (like hair style).:BOOLEAN`（1 次）
- `Include information about lighting.:BOOLEAN`（1 次）
- `Include information about camera angle.:BOOLEAN`（1 次）
- `Include information about whether there is a watermark or not.:BOOLEAN`（1 次）
- `Include information about whether there are JPEG artifacts or not.:BOOLEAN`（1 次）
- `If it is a photo you MUST include information about what camera was likely used and details such as aperture, shutter speed, ISO, etc.:BOOLEAN`（1 次）
- `Do NOT include anything sexual; keep it PG.:BOOLEAN`（1 次）
- `Do NOT mention the image's resolution.:BOOLEAN`（1 次）
- `You MUST include information about the subjective aesthetic quality of the image from low to very high.:BOOLEAN`（1 次）

## 输出

- `Extra_Options:Extra_Options`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
