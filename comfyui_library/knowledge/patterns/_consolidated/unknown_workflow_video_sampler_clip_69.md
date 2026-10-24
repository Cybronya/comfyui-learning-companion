---
name: unknown_workflow_video_sampler_clip_69
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.610222
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, GetNode, ImageResizeKJv2, Int, KSampler, PreviewImage, SetNode, SimpleMath+, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/动作迁移+长时间35秒+低显存24G，注意完整35S视频运行时间超过50分钟_2012570543026872321.json, 视频生成/图生视频/动作迁移_优化版_24G_排版，背景不保留_2004774742836080642.json, 视频生成/图生视频/动作迁移一致性保持效果好 Wan2.2 Animate_2016529777426964481.json, 视频生成/图生视频/动作迁移一致性完美保持 Wan2.2 Animate_2029839863943532545.json, 视频生成/图生视频/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）_2034116840758190081.json, 视频生成/图生视频/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）_2039924877129424898.json, 视频生成/图生视频/动作迁移，推理超级牛，长视频专属 Wan2.2 Animate_2001179799357976578.json, 视频生成/图生视频/可用动作迁移+长时间35秒+低显存24G_2034108510497148930.json, 视频生成/图生视频/模特服装批量动作迁移工作流-分段式迁移_2038704209280897026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/动作迁移+长时间35秒+低显存24G，注意完整35S视频运行时间超过50分钟_2012570543026872321.json、视频生成/图生视频/动作迁移_优化版_24G_排版，背景不保留_2004774742836080642.json、视频生成/图生视频/动作迁移一致性保持效果好 Wan2.2 Animate_2016529777426964481.json、视频生成/图生视频/动作迁移一致性完美保持 Wan2.2 Animate_2029839863943532545.json、视频生成/图生视频/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）_2034116840758190081.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `KSampler`
- `PreviewImage`
- `SetNode`
- `SimpleMath+`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 8/9 个有
- `GetImageRangeFromBatch` —— 7/9 个有
- `ImageBatchMulti` —— 7/9 个有
- `VHS_GetImageCount` —— 7/9 个有
- `DWPreprocessor` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `ModelSamplingSD3` —— 6/9 个有
- `PoseAndFaceDetection` —— 6/9 个有
- `RHHiddenNodes` —— 6/9 个有
- `UNETLoader` —— 6/9 个有
- `Display Int (rgthree)` —— 3/9 个有
- `DrawViTPose` —— 3/9 个有
- `ImageFromBatch` —— 3/9 个有
- `ImageScale` —— 3/9 个有
- `OnnxDetectionModelLoader` —— 3/9 个有
- `RMBG` —— 3/9 个有
- `easy batchAnything` —— 3/9 个有
- `CRTFirstLastFrameSelector` —— 2/9 个有
- `easy float` —— 2/9 个有
- `easy imageCount` —— 2/9 个有
- `CR Prompt Text` —— 1/9 个有
- `HAIGC_LoadImagesFromZip` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `PixelPerfectResolution` —— 1/9 个有
- `easy forLoopEnd` —— 1/9 个有
- `easy forLoopStart` —— 1/9 个有
- `easy imageListToImageBatch` —— 1/9 个有
- `easy int` —— 1/9 个有
- `easy showAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 9 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，9 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（33/9 个样本）：Steps较低可能导致细节不足
