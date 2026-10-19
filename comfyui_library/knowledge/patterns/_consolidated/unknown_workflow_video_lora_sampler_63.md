---
name: unknown_workflow_video_lora_sampler_63
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.636611
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, GetImageRangeFromBatch, GetNode, ImageBatchMulti, ImageResizeKJv2, Int, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, SimpleMath+, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2008225222398316546.json, 视频生成/图生视频/2002747679463620610.json, 视频生成/图生视频/2020050725358804994.json, 视频生成/图生视频/2037056894430351361.json, 视频生成/图生视频/2031640030707458050.json, 视频生成/图生视频/2071443164606586881.json, 视频生成/图生视频/1995377555693875202.json, 视频生成/图生视频/2033946576439218177.json, 视频生成/图生视频/2051245118031704065.json, 视频生成/图生视频/2017780725273075713.json, 视频生成/图生视频/2052037112278593537.json, 视频生成/图生视频/2009276664982806530.json, 视频生成/图生视频/2019196248963682306.json, 视频生成/图生视频/2024093081133391873.json, 视频生成/图生视频/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）+0_2079778626383466497.json, 视频生成/图生视频/2064595503089807361.json, 视频生成/图生视频/2052270105588973569.json, 视频生成/图生视频/2017778215057629185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_63

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/2008225222398316546.json、视频生成/图生视频/2002747679463620610.json、视频生成/图生视频/2020050725358804994.json、视频生成/图生视频/2037056894430351361.json、视频生成/图生视频/2031640030707458050.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `GetImageRangeFromBatch`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 17/18 个有
- `VHS_VideoInfoLoaded` —— 17/18 个有
- `Display Int (rgthree)` —— 16/18 个有
- `DrawViTPose` —— 16/18 个有
- `ImageScale` —— 16/18 个有
- `OnnxDetectionModelLoader` —— 16/18 个有
- `PoseAndFaceDetection` —— 16/18 个有
- `Primitive integer [Crystools]` —— 13/18 个有
- `easy float` —— 13/18 个有
- `PathchSageAttentionKJ` —— 12/18 个有
- `BatchCount+` —— 8/18 个有
- `ImageBatch` —— 8/18 个有
- `ImageFromBatch` —— 8/18 个有
- `RepeatImageBatch` —— 8/18 个有
- `easy mathInt` —— 8/18 个有
- `DWPreprocessor` —— 2/18 个有
- `RHHiddenNodes` —— 2/18 个有
- `ImageConcanate` —— 1/18 个有
- `LayerUtility: PurgeVRAM V2` —— 1/18 个有
- `Notif-PlaySound` —— 1/18 个有
- `RIFE VFI` —— 1/18 个有
- `SaveImage` —— 1/18 个有
- `ShellAgentPluginSaveAudios` —— 1/18 个有
- `TT_img_enc` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 57/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（57/18 个样本）：Steps较低可能导致细节不足
