---
name: unknown_workflow_lora_sampler_clip_65
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.780625
common_nodes: [BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveInt, RHLLMChatNode, StringReplace, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Bernini图像编辑_2065059800358154242.json, 图片生成/图生图/Bernini图像编辑v2_2064182005436342273.json, 图片生成/文生图/Bernini-R 图像编辑_2062541633941495810.json, 图片生成/文生图/Bernini-R 文生图_2062533470706036738.json, 平台全量/Bernini视频编辑还要调整_2064238115795070978.json, 平台全量/LTX2.3 3.5系列套件｜字幕水印去除_2067822291773378561.json, 平台全量/LTX2.3 Suite 3.5 Subtitle & Watermark Removal_2072998824693768192.json, 视频生成/文生视频/Bernini-R 文生视频_2062533464225837057.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Bernini图像编辑_2065059800358154242.json、图片生成/图生图/Bernini图像编辑v2_2064182005436342273.json、图片生成/文生图/Bernini-R 图像编辑_2062541633941495810.json、图片生成/文生图/Bernini-R 文生图_2062533470706036738.json、平台全量/Bernini视频编辑还要调整_2064238115795070978.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RHLLMChatNode`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Text` —— 6/8 个有
- `PreviewAny` —— 5/8 个有
- `CreateVideo` —— 4/8 个有
- `LoadImage` —— 4/8 个有
- `SaveImage` —— 4/8 个有
- `SaveVideo` —— 4/8 个有
- `JWInteger` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `image_scale_pixel_v2` —— 3/8 个有
- `GetVideoComponents` —— 2/8 个有
- `ImageFromBatch` —— 2/8 个有
- `LoadVideo` —— 2/8 个有
- `easy int` —— 2/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 62% |
| Prompt 约束强度(CFG) | 14 | 10 - 50 | 8 | 29% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 14，观测区间 10 - 50，8 个样本，取值分散，一致性仅 29%
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 50，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
