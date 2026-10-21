---
name: unknown_workflow_lora_sampler_clip_26
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.743556
common_nodes: [BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, PrimitiveInt, RHLLMChatNode, StringReplace, Text, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Bernini-R 图像编辑_2062541633941495810.json, 图片生成/文生图/Bernini-R 文生图_2062533470706036738.json, 视频生成/图生视频/2063268818142715906.json, 视频生成/图生视频/2063647431069356033.json, 视频生成/图生视频/2067591064046886913.json, 视频生成/文生视频/Bernini-R 3图参考成片工作流_2062503680565403649.json, 视频生成/文生视频/Bernini-R Image-to-Video_2072998885414707200.json, 视频生成/文生视频/Bernini-R 单图参考成片工作流_2062503688601690114.json, 视频生成/文生视频/Bernini-R 文生视频_2062533464225837057.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/Bernini-R 图像编辑_2062541633941495810.json、图片生成/文生图/Bernini-R 文生图_2062533470706036738.json、视频生成/图生视频/2063268818142715906.json、视频生成/图生视频/2063647431069356033.json、视频生成/图生视频/2067591064046886913.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 9 个 workflow 都包含：
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveInt`
- `RHLLMChatNode`
- `StringReplace`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/9 个有
- `image_scale_pixel_v2` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `PrimitiveFloat` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `BatchImagesNode` —— 3/9 个有
- `ImageScaleBy` —— 3/9 个有
- `RIFE VFI` —— 3/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `easy cleanGpuUsed` —— 3/9 个有
- `SaveImage` —— 2/9 个有
- `easy int` —— 2/9 个有
- `DF_Integer` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 9 | 100% |
| Prompt 约束强度(CFG) | 14 | 14 - 14 | 9 | 100% |
| 采样算法 | 1 | 1 - 1.5 | 9 | 81% |
| 调度器 | euler | - | 9 | 100% |
| 重绘幅度 | simple | - | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 14，观测区间 14 - 14，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.5，9 个样本，取值集中（一致性 81%）
- 调度器 最常用 euler，9 个样本，一致性 100%
- 重绘幅度 最常用 simple，9 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
