---
name: unknown_workflow_video_lora_sampler_386
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.63575
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, GetImageRangeFromBatch, GetNode, ImageBatchMulti, ImageResizeKJv2, Int, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, SetNode, SimpleMath+, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimateToVideo, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan2.2-Animate_修改版-长视频不变背景动作迁移-动作丝滑流畅速度快_2031979881122238466.json, 视频生成/图生视频/动作迁移 V4（人物一致性、面部表情、对口型、肢体手部优化、🐻部抖动优化版）_2017780725273075713.json, 视频生成/图生视频/动作迁移+面部捕捉（精细版）_2052037112278593537.json, 视频生成/图生视频/动作迁移全能版20260205_2019196248963682306.json, 视频生成/图生视频/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）+0_2079778626383466497.json, 视频生成/图生视频/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）_2034116840758190081.json, 视频生成/图生视频/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）_2039924877129424898.json, 视频生成/图生视频/模特服装批量动作迁移工作流-分段式迁移_2038704209280897026.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_386

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-Animate_修改版-长视频不变背景动作迁移-动作丝滑流畅速度快_2031979881122238466.json、视频生成/图生视频/动作迁移 V4（人物一致性、面部表情、对口型、肢体手部优化、🐻部抖动优化版）_2017780725273075713.json、视频生成/图生视频/动作迁移+面部捕捉（精细版）_2052037112278593537.json、视频生成/图生视频/动作迁移全能版20260205_2019196248963682306.json、视频生成/图生视频/动作迁移（一致性、表情、胸部调节，手部、胸部抖动优化版）+0_2079778626383466497.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 8 个 workflow 都包含：
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
- `VHS_VideoInfoLoaded`
- `WanAnimateToVideo`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Display Int (rgthree)` —— 7/8 个有
- `DrawViTPose` —— 7/8 个有
- `ImageScale` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `OnnxDetectionModelLoader` —— 7/8 个有
- `PoseAndFaceDetection` —— 7/8 个有
- `PreviewImage` —— 7/8 个有
- `easy float` —— 5/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `Primitive integer [Crystools]` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `DWPreprocessor` —— 1/8 个有
- `HAIGC_LoadImagesFromZip` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `ImageResize+` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `Notif-PlaySound` —— 1/8 个有
- `PrimitiveInt` —— 1/8 个有
- `RIFE VFI` —— 1/8 个有
- `ShellAgentPluginSaveAudios` —— 1/8 个有
- `easy batchAnything` —— 1/8 个有
- `easy forLoopEnd` —— 1/8 个有
- `easy forLoopStart` —— 1/8 个有
- `easy imageListToImageBatch` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 27/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（27/8 个样本）：Steps较低可能导致细节不足
