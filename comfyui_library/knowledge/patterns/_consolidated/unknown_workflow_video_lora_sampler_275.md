---
name: unknown_workflow_video_lora_sampler_275
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.95375
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/单图生视频_2083552023793979393.json, 视频生成/图生视频/图生视频 Aiwood wan2.2+2.1二阶_2033358933443747841.json, 视频生成/图生视频/图生视频工作流_2066459393683705858.json, 视频生成/图生视频/社区模型图生视频Smooth Mix i2V v2.0模型测试_2050537311854710785.json, 视频生成/图生视频/背摔视频特效wan2.2_1981669095458381825.json, 视频生成/图生视频/通义万相wan2.2图生视频（lightx2v加速6步）_1949968677410136066.json, 视频生成/图生视频/（自用）Wan2.2高质量图生视频工作流81帧50秒_1952579457632669698.json, 视频生成/图生视频/（（自用）官方版）Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1952589946924273666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_275

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/单图生视频_2083552023793979393.json、视频生成/图生视频/图生视频 Aiwood wan2.2+2.1二阶_2033358933443747841.json、视频生成/图生视频/图生视频工作流_2066459393683705858.json、视频生成/图生视频/社区模型图生视频Smooth Mix i2V v2.0模型测试_2050537311854710785.json、视频生成/图生视频/背摔视频特效wan2.2_1981669095458381825.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/8 个有
- `PathchSageAttentionKJ` —— 4/8 个有
- `LayerUtility: PurgeVRAM` —— 3/8 个有
- `CLIPVisionEncode` —— 2/8 个有
- `CLIPVisionLoader` —— 2/8 个有
- `LoadLatent` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `ConstrainImage|pysssss` —— 1/8 个有
- `GetImageSize+` —— 1/8 个有
- `SaveLatent` —— 1/8 个有
- `easy imageSize` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 62% |
| Prompt 约束强度(CFG) | 6 | 4 - 14 | 8 | 61% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 62% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 62%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 14，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 62%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
