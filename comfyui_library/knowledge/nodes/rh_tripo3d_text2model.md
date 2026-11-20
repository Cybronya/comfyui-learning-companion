# RH_Tripo3d_Text2Model

## 节点类型

`RH_Tripo3d_Text2Model`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `prompt:STRING`（2 次）
- `negative_prompt:STRING`（2 次）
- `model_version:COMBO`（2 次）
- `model_seed:INT`（2 次）
- `image_seed:INT`（2 次）
- `texture:BOOLEAN`（2 次）
- `pbr:BOOLEAN`（2 次）
- `texture_seed:INT`（2 次）
- `texture_quality:COMBO`（2 次）
- `texture_alignment:COMBO`（2 次）

## 输出

- `model_file:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["写实，科技感土星，一半是外星科技人造物一半是星球，C4D建模，Houdini渲染，细节刻画，", "low quality, blurry, noisy, distorted, low poly, rough mesh, bad top`（1 次）
- `["一匹歪脖子做鬼脸、极度夸张胖的的黄骠马，马腿细，背上骑着胖将军，Q版，唐代审美，C4D建模，blender渲染，细节刻画，玩偶", "low quality, blurry, noisy, distorted, low poly, ro`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
