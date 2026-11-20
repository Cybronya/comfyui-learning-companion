# Flux2KleinSectionedEncoder

## 节点类型

`Flux2KleinSectionedEncoder`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `clip:CLIP`（3 次）
- `mode:COMBO`（3 次）
- `front_text:STRING`（3 次）
- `mid_text:STRING`（3 次）
- `end_text:STRING`（3 次）
- `combined_prompt:STRING`（3 次）
- `separator:COMBO`（3 次）
- `show_preview:BOOLEAN`（3 次）
- `debug:BOOLEAN`（3 次）

## 输出

- `conditioning:CONDITIONING`（3 次）
- `front_section:STRING`（3 次）
- `mid_section:STRING`（3 次）
- `end_section:STRING`（3 次）
- `full_prompt:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["auto_balanced", "移除图像中的人物和所有与人体相关的特征（包括头部、四肢、面部和身体轮廓），仅保留人物所穿的衣物，不保留头饰。", "将衣物以平面俯拍（flat lay）的方式重新构图，保持衣物的原始款式、颜色、纹理、图`（1 次）
- `["auto_balanced", "保持角色的面部特征、身材比例和姿态不变，替换全身衣物。", "确保替换后的服装与角色原来的体型和身体结构完全匹配，颜色、材质和细节（如褶皱、纹理）与图2中的服装一致。", "输出为与原图分辨率相同的高清`（1 次）
- `["auto_balanced", "移除图像中的人物和所有与人体相关的特征（包括头部、四肢、面部和身体轮廓），仅保留人物所穿的衣物，不保留头饰。", "将衣物以平面俯拍（flat lay）的方式重新构图，保持衣物的原始款式、颜色、纹理、图`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
