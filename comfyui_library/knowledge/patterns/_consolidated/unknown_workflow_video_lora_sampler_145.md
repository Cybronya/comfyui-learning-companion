---
name: unknown_workflow_video_lora_sampler_145
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.904333
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, TextBox, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy int]
problems: []
missing: []
members: [视频生成/图生视频/1955215890101014529.json, 视频生成/图生视频/1952277132212948994.json, 视频生成/图生视频/1955503072236617730.json, 视频生成/图生视频/1955504798234656769.json, 视频生成/图生视频/1959204229682507777.json, 视频生成/图生视频/1959201352268328961.json, 视频生成/图生视频/1955506935590260737.json, 视频生成/图生视频/1955507451593310209.json, 视频生成/图生视频/1955509045698465793.json, 视频生成/图生视频/1955497249860194306.json, 视频生成/图生视频/1959203655159328769.json, 视频生成/图生视频/1955825577107210241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_145

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1955215890101014529.json、视频生成/图生视频/1952277132212948994.json、视频生成/图生视频/1955503072236617730.json、视频生成/图生视频/1955504798234656769.json、视频生成/图生视频/1959204229682507777.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `TextBox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `PrimitiveBoolean` —— 11/12 个有
- `easy cleanGpuUsed` —— 11/12 个有
- `easy showAnything` —— 11/12 个有
- `CLIPVisionEncode` —— 9/12 个有
- `CLIPVisionLoader` —— 9/12 个有
- `CR Text Replace` —— 9/12 个有
- `RH_Captioner` —— 9/12 个有
- `easy ifElse` —— 9/12 个有
- `RHHiddenNodes` —— 2/12 个有
- `RH_Translator` —— 2/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `QwenLoader` —— 1/12 个有
- `WanVideoPromptExtender` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 12 | 83% |
| Prompt 约束强度(CFG) | 8 | 8 - 12 | 12 | 83% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler | - | 12 | 83% |
| 重绘幅度 | simple | - | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，12 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 12，12 个样本，取值集中（一致性 83%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，12 个样本，一致性 83%
- 重绘幅度 最常用 simple，12 个样本，一致性 100%
