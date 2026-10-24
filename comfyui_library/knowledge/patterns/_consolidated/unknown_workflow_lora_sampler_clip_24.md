---
name: unknown_workflow_lora_sampler_clip_24
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.759818
common_nodes: [BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveInt, RHLLMChatNode, StringReplace, Text, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Bernini图像编辑_2065059800358154242.json, 图片生成/图生图/Bernini图像编辑v2_2064182005436342273.json, 图片生成/文生图/Bernini-R 图像编辑_2062541633941495810.json, 图片生成/文生图/Bernini-R 文生图_2062533470706036738.json, 视频生成/图生视频/Bernini-R 单图参考成片工作流_2063268818142715906.json, 视频生成/图生视频/Bernini-R 单图参考成片工作流_2063647431069356033.json, 视频生成/图生视频/Bernini-R 单图片段（言出法随 ）_2067591064046886913.json, 视频生成/文生视频/Bernini-R 3图参考成片工作流_2062503680565403649.json, 视频生成/文生视频/Bernini-R Image-to-Video_2072998885414707200.json, 视频生成/文生视频/Bernini-R 单图参考成片工作流_2062503688601690114.json, 视频生成/文生视频/Bernini-R 文生视频_2062533464225837057.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Bernini图像编辑_2065059800358154242.json、图片生成/图生图/Bernini图像编辑v2_2064182005436342273.json、图片生成/文生图/Bernini-R 图像编辑_2062541633941495810.json、图片生成/文生图/Bernini-R 文生图_2062533470706036738.json、视频生成/图生视频/Bernini-R 单图参考成片工作流_2063268818142715906.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 11 个 workflow 都包含：
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
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/11 个有
- `PreviewAny` —— 9/11 个有
- `image_scale_pixel_v2` —— 7/11 个有
- `CreateVideo` —— 6/11 个有
- `PrimitiveFloat` —— 6/11 个有
- `SaveVideo` —— 6/11 个有
- `SaveImage` —— 4/11 个有
- `BatchImagesNode` —— 3/11 个有
- `ImageScaleBy` —— 3/11 个有
- `RIFE VFI` —— 3/11 个有
- `VHS_VideoCombine` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `JWInteger` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `easy int` —— 2/11 个有
- `DF_Integer` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 82% |
| Prompt 约束强度(CFG) | 14 | 14 - 50 | 11 | 32% |
| 采样算法 | 1 | 1 - 1.5 | 11 | 82% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 82%
- Prompt 约束强度(CFG) 中位数 14，观测区间 14 - 50，11 个样本，取值分散，一致性仅 32%
- 采样算法 中位数 1，观测区间 1 - 1.5，11 个样本，取值集中（一致性 82%）
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 50，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
