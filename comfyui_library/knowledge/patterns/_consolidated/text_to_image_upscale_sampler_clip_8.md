---
name: text_to_image_upscale_sampler_clip_8
type: Text To Image
frequency: 11
level: strong
coverage: 0.759
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Ai漫剧角色设计 文生图+全节点注释_2077736737903833089.json, 图片生成/文生图/Ai漫剧角色设计 文生图+全节点注释_2083833403341885441.json, 图片生成/文生图/Seedance专属 • 超级角色定妆照：定格工业级角色美学巅峰_文生图_角色设计_2035558558393176065.json, 图片生成/文生图/boogu turbo反推文生图+seedvr2高清放大_2070365724652171265.json, 图片生成/文生图/boogu turbo反推文生图+seedvr2高清放大_2070401740339499010.json, 图片生成/文生图/boogu turbo反推文生图+seedvr2高清放大_2070425980388335617.json, 图片生成/文生图/krea2反推文生图+seedvr2高清放大_2070358712178528257.json, 图片生成/文生图/krea2反推文生图+seedvr2高清放大_2070399890324279298.json, 图片生成/文生图/krea2反推文生图+seedvr2高清放大_2070413403033788418.json, 图片生成/文生图/krea2反推文生图+seedvr2高清放大_2070427327246454785.json, 图片生成/文生图/超级角色定妆照：定格工业级角色美学巅峰_文生图_角色设计_2083838238770421762.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_8

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Ai漫剧角色设计 文生图+全节点注释_2077736737903833089.json、图片生成/文生图/Ai漫剧角色设计 文生图+全节点注释_2083833403341885441.json、图片生成/文生图/Seedance专属 • 超级角色定妆照：定格工业级角色美学巅峰_文生图_角色设计_2035558558393176065.json、图片生成/文生图/boogu turbo反推文生图+seedvr2高清放大_2070365724652171265.json、图片生成/文生图/boogu turbo反推文生图+seedvr2高清放大_2070401740339499010.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 9/11 个有
- `LoadImage` —— 9/11 个有
- `PreviewImage` —— 9/11 个有
- `AILab_QwenVL` —— 7/11 个有
- `CR Text` —— 7/11 个有
- `PrimitiveInt` —— 7/11 个有
- `INTConstant` —— 4/11 个有
- `ImpactInt` —— 4/11 个有
- `KOOK_ImageCompression` —— 4/11 个有
- `LoraLoaderModelOnly` —— 4/11 个有
- `PreviewAny` —— 4/11 个有
- `RH_LLMAPI_Pro_Node` —— 4/11 个有
- `ImageListToImageBatch` —— 2/11 个有
- `RH_LLMAPI_NODE` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1024 | 11 | 84% |
| 高度 | 1536 | 1280 - 1536 | 11 | 91% |
| 采样步数 | 8 | 8 - 9 | 11 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | res_2s | - | 11 | 36% |
| 调度器 | simple | - | 11 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1024，11 个样本，取值集中（一致性 84%）
- 高度 中位数 1536，观测区间 1280 - 1536，11 个样本，取值集中（一致性 91%）
- 采样步数 中位数 8，观测区间 8 - 9，11 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，11 个样本，一致性 36%
- 调度器 最常用 simple，11 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
