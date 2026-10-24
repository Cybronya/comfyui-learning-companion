---
name: unknown_workflow_video_lora_sampler_115
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.576615
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetNode, GrowMask, ImageBlend, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewImage, PrimitiveFloat, SetNode, TorchCompileModelWanVideoV2, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【视频换人】Animate +Sec扣图换人_1978713604222554114.json, 图片生成/文生图/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1978479937873137665.json, 视频生成/图生视频/Animate +Sec扣图节点 --动作迁移、人物替换 -- 想换哪里换哪里_1979733703280726017.json, 视频生成/图生视频/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1977883468296245249.json, 视频生成/图生视频/AnimateV2遮罩升级版SeC人物替换_1977328876730896386.json, 视频生成/图生视频/Wan-Animatev2.2_1971886781874499586.json, 视频生成/图生视频/Wan-Animate全自动版_1976469755416715266.json, 视频生成/图生视频/WanAnimateV2SEC自动遮罩_1978107415881211906.json, 视频生成/图生视频/Work-Fisher_Wan-Animate全自动版_1969348581830389761.json, 视频生成/图生视频/YZ金鱼-Wan Animate_Mix_官方版_v2.2_1971377068741214210.json, 视频生成/图生视频/动作迁移+角色替换二合一官方工作流（小显存、速度快、质量好）_2077716276075651074.json, 视频生成/图生视频/最新Wan Animate 动作迁移+人物替换  新遮罩SEC 更精准 想换哪换哪_1980798178817654785.json, 视频生成/图生视频/视频主体替换可切镜头Wan-Animate_1974073338375090178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_115

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/【视频换人】Animate +Sec扣图换人_1978713604222554114.json、图片生成/文生图/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1978479937873137665.json、视频生成/图生视频/Animate +Sec扣图节点 --动作迁移、人物替换 -- 想换哪里换哪里_1979733703280726017.json、视频生成/图生视频/Animate 动作迁移 人物替换 终极整合官方版 新遮罩 更精准_1977883468296245249.json、视频生成/图生视频/AnimateV2遮罩升级版SeC人物替换_1977328876730896386.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 13 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `GrowMask`
- `ImageBlend`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `PreviewImage`
- `PrimitiveFloat`
- `SetNode`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `UnetLoaderGGUF` —— 10/13 个有
- `Fast Groups Bypasser (rgthree)` —— 8/13 个有
- `INTConstant` —— 8/13 个有
- `ImageConcatMulti` —— 8/13 个有
- `easy showAnything` —— 8/13 个有
- `PlaySound|pysssss` —— 7/13 个有
- `SeCModelLoader` —— 7/13 个有
- `SeCVideoSegmentation` —— 7/13 个有
- `EmptyImage` —— 6/13 个有
- `ImageRemoveBackground+` —— 6/13 个有
- `PointsEditor` —— 6/13 个有
- `RemBGSession+` —— 6/13 个有
- `UNETLoader` —— 6/13 个有
- `CR Model Input Switch` —— 5/13 个有
- `DownloadAndLoadGIMMVFIModel` —— 5/13 个有
- `Fast Bypasser (rgthree)` —— 5/13 个有
- `GIMMVFI_interpolate` —— 5/13 个有
- `ImpactInt` —— 5/13 个有
- `LayerUtility: PurgeVRAM` —— 5/13 个有
- `Mute / Bypass Repeater (rgthree)` —— 5/13 个有
- `SimpleMath+` —— 5/13 个有
- `easy convertAnything` —— 5/13 个有
- `easy int` —— 5/13 个有
- `GGUFLoaderKJ` —— 3/13 个有
- `JjkText` —— 2/13 个有
- `RIFE VFI` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `ImageFromBatch` —— 1/13 个有
- `ImageResizeKJ` —— 1/13 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `SaveImage` —— 1/13 个有
- `TT_img_enc_v2` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | sa_solver | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
