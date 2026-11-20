---
name: unknown_workflow_video_lora_clip_3
type: Unknown Workflow
frequency: 30
level: strong
coverage: 0.9119
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, CLIPVisionEncode, DrawViTPose, GetImageRangeFromBatch, GetImageSize, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, SimpleMath+, SimpleMathDual+, TorchCompileModelWanVideoV2, TrimVideoLatent, VAEDecode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanAnimateToVideo, easy batchAnything, easy boolean, easy compare, easy convertAnything, easy ifElse, easy int, easy lengthAnything, easy positive, easy promptReplace, easy whileLoopEnd, easy whileLoopStart, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/8dkapdfjber_2059685374263390210.json, 图片生成/反推提示词/8ftcwbbbfez_2059689489123069954.json, 图片生成/反推提示词/8ofkrdcdllz_2059883096257949697.json, 图片生成/反推提示词/8wglxbytrjd_2059885864880271362.json, 图片生成/反推提示词/8xxudkrcaru_2059885207356006402.json, 图片生成/反推提示词/8yijianqianyimikez_2048692743072911361.json, 图片生成/图生图/动作迁移9999_1990918130933374978.json, 图片生成/图生图/动作迁移升级版+表情+动作+不限时长+舞蹈动作模仿+各种动作复刻参考+图生视频_2115624678915141634.json, 图片生成/图生图/动作迁移升级版+表情+动作+不限时长+舞蹈动作模仿+各种动作复刻参考+图生视频_2115670557319581698.json, 平台全量/AI视频丨Wan2.2 Animate丨视频生成_2119627464539467777.json, 平台全量/F动作迁移+表情+动作+不限时长+舞蹈动作模仿+各种动作复刻参考_2047639134168158209.json, 平台全量/SteadyDancer超强动作迁移_2074729790652899329.json, 平台全量/SteadyDancer超强动作迁移_2074835087992119298.json, 平台全量/动作迁移_1976268842445967361.json, 平台全量/动作迁移升级版+表情+动作+不限时长+舞蹈动作模仿+各种动作复刻参考+图生视频_2021907990386843650.json, 平台全量/动作迁移升级版+表情+动作+不限时长+舞蹈动作模仿+各种动作复刻参考+图生视频_2067216932130086913.json, 平台全量/动作迁移升级版+表情+动作+不限时长+舞蹈动作模仿+各种动作复刻参考图生视频_2119055198105722881.json, 平台全量/动作迁移升级版+表情+动作+不限时长+舞蹈动作模仿+各种动作复刻参考图生视频_2119350602831585281.json, 平台全量/动作迁移升级版+表情+动作+不限时长+舞蹈动作模仿_2050171548186755074.json, 平台全量/动作迁移可手动分割_2007856656067076098.json, 平台全量/各大平台热门AI美女跳舞工作流（人物一致性换脸+修手+运镜）_1896565421057671169.json, 平台全量/唐SIR-一键换装-动作迁移（舞蹈版）全自动化_2038630039603908609.json, 平台全量/最强人物驱动工作流V3（更好的遮罩)_2010919988617551873.json, 平台全量/浮云 动作迁移_1993572328642723842.json, 平台全量/空白工作流_2061523579317088257.json, 平台全量/超好用的动作迁移wan22Animate_2020680193530138625.json, 平台全量/超强动作迁移_2069442605942927362.json, 平台全量/超强动作迁移_2069450384766230530.json, 平台全量/超强动作迁移_2073769307158433794.json, 平台全量/（有问题）animate KJ V2动作迁移_2010158340306898945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_3

> 由 `engine/knowledge_consolidation` 从 30 个 workflow 归纳得出（图片生成/反推提示词/8dkapdfjber_2059685374263390210.json、图片生成/反推提示词/8ftcwbbbfez_2059689489123069954.json、图片生成/反推提示词/8ofkrdcdllz_2059883096257949697.json、图片生成/反推提示词/8wglxbytrjd_2059885864880271362.json、图片生成/反推提示词/8xxudkrcaru_2059885207356006402.json…）

- **类型**：Unknown Workflow
- **样本数**：30
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 30 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `SimpleMath+`
- `SimpleMathDual+`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanAnimateToVideo`
- `easy batchAnything`
- `easy boolean`
- `easy compare`
- `easy convertAnything`
- `easy ifElse`
- `easy int`
- `easy lengthAnything`
- `easy positive`
- `easy promptReplace`
- `easy whileLoopEnd`
- `easy whileLoopStart`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 28/30 个有
- `SaveVideoRGBA` —— 28/30 个有
- `RHHiddenNodes` —— 27/30 个有
- `CLIPVisionLoader` —— 24/30 个有
- `Seed` —— 24/30 个有
- `UNETLoader` —— 24/30 个有
- `VAELoader` —— 24/30 个有
- `BlockifyMask` —— 23/30 个有
- `DrawMaskOnImage` —— 23/30 个有
- `Fast Groups Muter (rgthree)` —— 23/30 个有
- `GrowMask` —— 23/30 个有
- `MathExpression|pysssss` —— 23/30 个有
- `PointsEditor` —— 23/30 个有
- `DownloadAndLoadSAM2Model` —— 22/30 个有
- `LayerUtility: ImageBlend` —— 22/30 个有
- `Sam2Segmentation` —— 22/30 个有
- `ImageResizeKJv2` —— 20/30 个有
- `KSampler` —— 20/30 个有
- `FlashVSRNode` —— 12/30 个有
- `Int` —— 12/30 个有
- `Text` —— 6/30 个有
- `ShellAgentPluginOutputText` —— 5/30 个有
- `ImpactSwitch` —— 2/30 个有
- `SaveImage` —— 2/30 个有
- `easy cleanGpuUsed` —— 2/30 个有
- `AnyBooleanSwitch` —— 1/30 个有
- `AudioCrop` —— 1/30 个有
- `CR Text` —— 1/30 个有
- `CompressImages` —— 1/30 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/30 个有
- `Fast Groups Bypasser (rgthree)` —— 1/30 个有
- `FileNamePrefix` —— 1/30 个有
- `GIMMVFI_interpolate` —— 1/30 个有
- `ImageBlend` —— 1/30 个有
- `ImpactInversedSwitch` —— 1/30 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/30 个有
- `LoadAudio` —— 1/30 个有
- `PreviewAny` —— 1/30 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/30 个有
- `SeCModelLoader` —— 1/30 个有
- `SeCVideoSegmentation` —— 1/30 个有
- `VideoCombineNode` —— 1/30 个有
- `easy clearCacheAll` —— 1/30 个有
- `孤海注释` —— 1/30 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 20 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 20 | 100% |
| 采样算法 | sa_solver | - | 20 | 100% |
| 调度器 | linear_quadratic | - | 20 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/30 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，20 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，20 个样本，一致性 100%
- 调度器 最常用 linear_quadratic，20 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
- 高发问题（20/30 个样本）：Steps较低可能导致细节不足
