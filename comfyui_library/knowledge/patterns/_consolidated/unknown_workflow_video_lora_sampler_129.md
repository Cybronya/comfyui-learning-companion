---
name: unknown_workflow_video_lora_sampler_129
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.456933
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, Fast Groups Bypasser (rgthree), GetNode, GrowMask, ImageBlend, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewImage, PrimitiveFloat, SetNode, TorchCompileModelWanVideoV2, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Wan-Animate全自动版_1978389452143923202.json, 平台全量/Work-Fisher-AnimateV2多人手动SEC遮罩版_1977088247786557442.json, 平台全量/Work-Fisher-Animate自动V2版_1977241098026405890.json, 平台全量/Z-AnimateV2遮罩指定人物替换_1984876640247365633.json, 平台全量/官方版  Wan animate_Mix_主体替换（自动遮罩）_1972990928380145666.json, 平台全量/换脸_2034128807807950850.json, 视频生成/图生视频/AnimateV2遮罩升级版SeC人物替换_1977328876730896386.json, 视频生成/图生视频/Wan-Animatev2.2_1971886781874499586.json, 视频生成/图生视频/Wan-Animate全自动版_1976469755416715266.json, 视频生成/图生视频/WanAnimateV2SEC自动遮罩_1978107415881211906.json, 视频生成/图生视频/Work-Fisher_Wan-Animate全自动版_1969348581830389761.json, 视频生成/图生视频/YZ金鱼-Wan Animate_Mix_官方版_v2.2_1971377068741214210.json, 视频生成/图生视频/动作迁移+角色替换二合一官方工作流（小显存、速度快、质量好）_2077716276075651074.json, 视频生成/图生视频/更换视频人物【动作】【五官】【一致】+手动遮罩_2008366086382690306.json, 视频生成/图生视频/视频主体替换可切镜头Wan-Animate_1974073338375090178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_129

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/反推提示词/Wan-Animate全自动版_1978389452143923202.json、平台全量/Work-Fisher-AnimateV2多人手动SEC遮罩版_1977088247786557442.json、平台全量/Work-Fisher-Animate自动V2版_1977241098026405890.json、平台全量/Z-AnimateV2遮罩指定人物替换_1984876640247365633.json、平台全量/官方版  Wan animate_Mix_主体替换（自动遮罩）_1972990928380145666.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 15 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GrowMask`
- `ImageBlend`
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
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 14/15 个有
- `ImageResizeKJv2` —— 14/15 个有
- `PlaySound|pysssss` —— 12/15 个有
- `ImageRemoveBackground+` —— 10/15 个有
- `RemBGSession+` —— 10/15 个有
- `UnetLoaderGGUF` —— 10/15 个有
- `EmptyImage` —— 9/15 个有
- `DownloadAndLoadGIMMVFIModel` —— 6/15 个有
- `GIMMVFI_interpolate` —— 6/15 个有
- `ImageConcatMulti` —— 6/15 个有
- `RIFE VFI` —— 6/15 个有
- `GGUFLoaderKJ` —— 5/15 个有
- `SeCModelLoader` —— 5/15 个有
- `SeCVideoSegmentation` —— 5/15 个有
- `easy cleanGpuUsed` —— 5/15 个有
- `PointsEditor` —— 4/15 个有
- `ImageFromBatch` —— 2/15 个有
- `CR Prompt Text` —— 1/15 个有
- `ClothesSegment` —— 1/15 个有
- `Int` —— 1/15 个有
- `JWInteger` —— 1/15 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `MaskPreview+` —— 1/15 个有
- `MathExpression_UTK` —— 1/15 个有
- `PreviewAny` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有
- `SaveImage` —— 1/15 个有
- `TT_img_enc_v2` —— 1/15 个有
- `UNETLoader` —— 1/15 个有
- `VHS_VideoInfoSource` —— 1/15 个有
- `easy imageInterrogator` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | sa_solver | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
