# UnofficialExtensions

## 节点类型

`UnofficialExtensions`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `adain_on_v:BOOLEAN`（3 次）
- `post_attention_adain_strength:FLOAT`（3 次）
- `axis0_rope_mode:COMBO`（3 次）
- `axis0_rope_scale:FLOAT`（3 次）
- `orthogonal_v_injection:FLOAT`（3 次）

## 输出

- `unofficial_extensions:UNTWISTING_ROPE_EXTENSIONS`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 0.5, "match_axes", 1, 0.5000000000000001]`（2 次）
- `[true, 0.5, "match_axes", 1, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
