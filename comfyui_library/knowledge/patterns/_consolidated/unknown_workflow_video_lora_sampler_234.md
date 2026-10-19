---
name: unknown_workflow_video_lora_sampler_234
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.892667
common_nodes: [Any To Any, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, CreateVideo, GetVideoComponents, HunyuanVideoFoley, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, Qwen3_VQA, RHLLMChatNode, StringReplace, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2069963218600161282.json, 视频生成/图生视频/2069956423366307842.json, 视频生成/图生视频/2069779286491484161.json, 视频生成/图生视频/2067419048618577922.json, 视频生成/图生视频/2073466231541293057.json, 视频生成/图生视频/2073466320544423937.json, 视频生成/文生视频/Bernini文生视频+音效v3_2064182065469415426.json, 视频生成/文生视频/Bernin文生视频+音效v3_2065034781892636673.json, 视频生成/文生视频/开源最强 全模态图生视频V3 单音效版：Bernini_2073747005947604994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_234

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2069963218600161282.json、视频生成/图生视频/2069956423366307842.json、视频生成/图生视频/2069779286491484161.json、视频生成/图生视频/2067419048618577922.json、视频生成/图生视频/2073466231541293057.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `Any To Any`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetVideoComponents`
- `HunyuanVideoFoley`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `Qwen3_VQA`
- `RHLLMChatNode`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SaveVideo` —— 8/9 个有
- `LoadImage` —— 7/9 个有
- `CR Prompt Text` —— 6/9 个有
- `Text` —— 6/9 个有
- `ImageResizeKJv2` —— 5/9 个有
- `PrimitiveInt` —— 5/9 个有
- `JWInteger` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `SimpleMath+` —— 4/9 个有
- `Any Switch (rgthree)` —— 3/9 个有
- `CR Text` —— 3/9 个有
- `DF_Int_to_Float` —— 3/9 个有
- `DF_Integer` —— 3/9 个有
- `Fast Groups Muter (rgthree)` —— 3/9 个有
- `Image Batch` —— 3/9 个有
- `MaxNode` —— 3/9 个有
- `BatchImagesNode` —— 2/9 个有
- `easy int` —— 2/9 个有
- `Int` —— 1/9 个有
- `intToFloat _O` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 100% |
| Prompt 约束强度(CFG) | 10 | 4 - 10 | 9 | 65% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 4 - 10，9 个样本
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
