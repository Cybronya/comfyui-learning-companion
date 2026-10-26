---
name: unknown_workflow_video_lora_sampler_369
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.901143
common_nodes: [Any To Any, BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, CreateVideo, GetVideoComponents, HunyuanVideoFoley, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, Qwen3_VQA, RHLLMChatNode, StringReplace, UNETLoader, VAEDecode, VAELoader, VHS_SelectFilename, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Wan22-Bernini单参考图生视频（自动音效 _ 双模式提示词）_2069963218600161282.json, 视频生成/图生视频/Wan22-Bernini双参考图生视频（自动音效 _ 双模式提示词）_2069956423366307842.json, 视频生成/图生视频/Wan22-Bernini多参考图生视频（自动音效 _ 双模式提示词）_2069779286491484161.json, 视频生成/文生视频/Bernini文生视频+音效v3_2064182065469415426.json, 视频生成/文生视频/Bernin文生视频+音效v3_2065034781892636673.json, 视频生成/文生视频/开源最强 全模态图生视频V3 单音效版：Bernini_2073747005947604994.json, 视频生成/文生视频/（4步加速版）Bernini文生视频+音效v3_2073465929488490497.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_369

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan22-Bernini单参考图生视频（自动音效 _ 双模式提示词）_2069963218600161282.json、视频生成/图生视频/Wan22-Bernini双参考图生视频（自动音效 _ 双模式提示词）_2069956423366307842.json、视频生成/图生视频/Wan22-Bernini多参考图生视频（自动音效 _ 双模式提示词）_2069779286491484161.json、视频生成/文生视频/Bernini文生视频+音效v3_2064182065469415426.json、视频生成/文生视频/Bernin文生视频+音效v3_2065034781892636673.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
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
- `SaveVideo` —— 6/7 个有
- `CR Prompt Text` —— 4/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `LoadImage` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `Text` —— 4/7 个有
- `Any Switch (rgthree)` —— 3/7 个有
- `CR Text` —— 3/7 个有
- `DF_Int_to_Float` —— 3/7 个有
- `DF_Integer` —— 3/7 个有
- `Fast Groups Muter (rgthree)` —— 3/7 个有
- `Image Batch` —— 3/7 个有
- `MaxNode` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `easy int` —— 3/7 个有
- `BatchImagesNode` —— 1/7 个有
- `Int` —— 1/7 个有
- `JWInteger` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `intToFloat _O` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 10 | 4 - 10 | 7 | 67% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 4 - 10，7 个样本
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
