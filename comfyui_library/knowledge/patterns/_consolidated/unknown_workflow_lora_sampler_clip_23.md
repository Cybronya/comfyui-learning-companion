---
name: unknown_workflow_lora_sampler_clip_23
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.74975
common_nodes: [BerniniConditioning, BerniniPromptEnhancer, CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoraLoaderModelOnly, PathchSageAttentionKJ, PrimitiveInt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2063268818142715906.json, 视频生成/图生视频/2063647431069356033.json, 视频生成/图生视频/2065245027042947073.json, 视频生成/图生视频/2067591064046886913.json, 视频生成/文生视频/Bernini-R 3图参考成片工作流_2062503680565403649.json, 视频生成/文生视频/Bernini-R Image-to-Video_2072998885414707200.json, 视频生成/文生视频/Bernini-R 单图参考成片工作流_2062503688601690114.json, 视频生成/文生视频/Bernini-R 文生视频_2062533464225837057.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2063268818142715906.json、视频生成/图生视频/2063647431069356033.json、视频生成/图生视频/2065245027042947073.json、视频生成/图生视频/2067591064046886913.json、视频生成/文生视频/Bernini-R 3图参考成片工作流_2062503680565403649.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：75%

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
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `PrimitiveFloat` —— 7/8 个有
- `RHLLMChatNode` —— 7/8 个有
- `StringReplace` —— 7/8 个有
- `Text` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `SaveVideo` —— 6/8 个有
- `image_scale_pixel_v2` —— 6/8 个有
- `RIFE VFI` —— 4/8 个有
- `VHS_VideoCombine` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `BatchImagesNode` —— 3/8 个有
- `ImageScaleBy` —— 3/8 个有
- `DF_Integer` —— 1/8 个有
- `FlashVSRNode` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 100% |
| Prompt 约束强度(CFG) | 14 | 14 - 14 | 8 | 100% |
| 采样算法 | 1 | 1 - 1.5 | 8 | 81% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 14，观测区间 14 - 14，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1.5，8 个样本，取值集中（一致性 81%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
