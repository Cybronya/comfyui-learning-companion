# PromptRelaySmartEncode

## 节点类型

`PromptRelaySmartEncode`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `model:MODEL`（6 次）
- `clip:CLIP`（6 次）
- `latent:LATENT`（6 次）
- `global_prompt:STRING`（6 次）
- `smart_prompt:STRING`（6 次）
- `normalize_by_tokens:BOOLEAN`（6 次）
- `epsilon:FLOAT`（6 次）

## 输出

- `model:MODEL`（6 次）
- `positive:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", false, 0.001]`（2 次）
- `["在灯火阑珊、充满古风韵味的木质村落街头，三位身着优雅轻盈古装的少女——仙灵林、仙灵梅与仙灵悦，正共同开启一场梦幻的夜晚盛宴。镜头起始于仙灵林的近景，她怀抱毛绒小马，眼神中透着调皮与期待。随着她惊喜地捂嘴、灿烂地笑开，并充满激情地向观众宣`（1 次）
- `["A single continuous cinematic 10-second LTX-2.3 PromptRelay text-to-video shot of a modern Formula 1 car racing throug`（1 次）
- `["A single continuous cinematic 12-second LTX-2.3 PromptRelay multi-reference image-to-video shot. Use the provided refe`（1 次）
- `["A realistic cinematic 10-second image-to-video talking portrait based on the provided first frame. Preserve the same w`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
