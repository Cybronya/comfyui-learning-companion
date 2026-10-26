---
name: text_to_image_upscale_sampler_clip_5
type: Text To Image
frequency: 13
level: strong
coverage: 0.780923
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, RunningHub Deepcleaner, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Seedance专属 • 图生图超级角色定妆照：定格工业级角色美学巅峰_角色设计_2045365667511148545.json, 图片生成/图生图/Seedance专属 • 图生图超级角色定妆照：角色设计+角色延伸_2049056318056566785.json, 图片生成/文生图/Ai漫剧角色设计 文生图+全节点注释_2077736737903833089.json, 图片生成/文生图/Ai漫剧角色设计 文生图+全节点注释_2083833403341885441.json, 图片生成/文生图/Seedance专属 • 超级角色定妆照：定格工业级角色美学巅峰_文生图_角色设计_2035558558393176065.json, 图片生成/文生图/boogu turbo反推文生图+seedvr2高清放大_2070365724652171265.json, 图片生成/文生图/boogu turbo反推文生图+seedvr2高清放大_2070401740339499010.json, 图片生成/文生图/boogu turbo反推文生图+seedvr2高清放大_2070425980388335617.json, 图片生成/文生图/krea2反推文生图+seedvr2高清放大_2070358712178528257.json, 图片生成/文生图/krea2反推文生图+seedvr2高清放大_2070399890324279298.json, 图片生成/文生图/krea2反推文生图+seedvr2高清放大_2070413403033788418.json, 图片生成/文生图/krea2反推文生图+seedvr2高清放大_2070427327246454785.json, 图片生成/文生图/超级角色定妆照：定格工业级角色美学巅峰_文生图_角色设计_2083838238770421762.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Seedance专属 • 图生图超级角色定妆照：定格工业级角色美学巅峰_角色设计_2045365667511148545.json、图片生成/图生图/Seedance专属 • 图生图超级角色定妆照：角色设计+角色延伸_2049056318056566785.json、图片生成/文生图/Ai漫剧角色设计 文生图+全节点注释_2077736737903833089.json、图片生成/文生图/Ai漫剧角色设计 文生图+全节点注释_2083833403341885441.json、图片生成/文生图/Seedance专属 • 超级角色定妆照：定格工业级角色美学巅峰_文生图_角色设计_2035558558393176065.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 13 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 11/13 个有
- `LoadImage` —— 11/13 个有
- `PreviewImage` —— 11/13 个有
- `CR Text` —— 9/13 个有
- `AILab_QwenVL` —— 7/13 个有
- `PrimitiveInt` —— 7/13 个有
- `INTConstant` —— 6/13 个有
- `ImpactInt` —— 6/13 个有
- `KOOK_ImageCompression` —— 6/13 个有
- `LoraLoaderModelOnly` —— 6/13 个有
- `PreviewAny` —— 6/13 个有
- `RH_LLMAPI_Pro_Node` —— 6/13 个有
- `ImageListToImageBatch` —— 4/13 个有
- `RH_LLMAPI_NODE` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 720 - 1024 | 13 | 83% |
| 高度 | 1536 | 1280 - 1536 | 13 | 91% |
| 采样步数 | 8 | 8 - 9 | 13 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | res_2s | - | 13 | 46% |
| 调度器 | simple | - | 13 | 54% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 720 - 1024，13 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 1280 - 1536，13 个样本，取值集中（一致性 91%）
- 采样步数 中位数 8，观测区间 8 - 9，13 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，13 个样本，一致性 46%
- 调度器 最常用 simple，13 个样本，一致性 54%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
