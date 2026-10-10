# PromptRelayEncodeTimeline

## 节点类型

`PromptRelayEncodeTimeline`

## 分类

Encoding

## 作用

编码类节点：把数据编码为另一表示（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `clip:CLIP`（2 次）
- `latent:LATENT`（2 次）
- `global_prompt:STRING`（2 次）
- `max_frames:INT`（2 次）
- `timeline_data:STRING`（2 次）
- `local_prompts:STRING`（2 次）
- `segment_lengths:STRING`（2 次）
- `epsilon:FLOAT`（2 次）
- `fps:FLOAT`（2 次）

## 输出

- `model:MODEL`（2 次）
- `positive:CONDITIONING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Anime battle sequence, 90s aesthetic, cel-shaded style. strong character consistency across all shots, dramatic compos`（1 次）
- `["Japanese Anime scenes , Mei gets caught in heavy rain on her way to the antique shop. Ren suddenly appears with a big `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
