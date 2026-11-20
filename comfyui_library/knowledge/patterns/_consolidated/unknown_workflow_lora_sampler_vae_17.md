---
name: unknown_workflow_lora_sampler_vae_17
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.9445
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, Text Load Line From File, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader, easy batchAnything, easy forLoopEnd, easy forLoopStart]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/人物15个多视角生成_2008060893489270786.json, 图片生成/图生图/人物15个多视角生成（数据集必备）_1995334886917595138.json, 平台全量/人物模特全视图  角色一致性 角色 人物一致性 姿态迁移   Qwen-Edit_2511_2009426464378200066.json, 平台全量/全视图 _ 角色一致性 V2_1868872246126084098.json, 平台全量/角色三视图 模特人物多视角 +SeedVR2 高清放大 多视图 角色多视角 Qwen_2076840383732076546.json, 视频生成/文生视频/三视图_多视图_角色三视图_角色多视角_Qwen_2045155129598418945.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_vae_17

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/人物15个多视角生成_2008060893489270786.json、图片生成/图生图/人物15个多视角生成（数据集必备）_1995334886917595138.json、平台全量/人物模特全视图  角色一致性 角色 人物一致性 姿态迁移   Qwen-Edit_2511_2009426464378200066.json、平台全量/全视图 _ 角色一致性 V2_1868872246126084098.json、平台全量/角色三视图 模特人物多视角 +SeedVR2 高清放大 多视图 角色多视角 Qwen_2076840383732076546.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `Text Load Line From File`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`

**可变部分**（部分 workflow 才有）：
- `MathExpression|pysssss` —— 4/6 个有
- `ModelPatchTorchSettings` —— 4/6 个有
- `NunchakuQwenImageDiTLoader` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `TextEncodeQwenImageEdit` —— 4/6 个有
- `easy anythingIndexSwitch` —— 4/6 个有
- `Any Switch (rgthree)` —— 2/6 个有
- `GGUFLoaderKJ` —— 2/6 个有
- `Label (rgthree)` —— 2/6 个有
- `SeedVR2LoadDiTModel` —— 2/6 个有
- `SeedVR2LoadVAEModel` —— 2/6 个有
- `SeedVR2VideoUpscaler` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `easy imageBatchToImageList` —— 2/6 个有
- `easy imageListToImageBatch` —— 2/6 个有
- `Fast Bypasser (rgthree)` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 720 - 1024 | 6 | 84% |
| 高度 | 1440 | 1024 - 1448 | 6 | 85% |
| 采样步数 | 4 | 4 - 8 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 720 - 1024，6 个样本，取值集中（一致性 84%）
- 高度 中位数 1440，观测区间 1024 - 1448，6 个样本，取值集中（一致性 85%）
- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
