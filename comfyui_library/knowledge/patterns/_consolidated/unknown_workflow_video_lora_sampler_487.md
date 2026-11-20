---
name: unknown_workflow_video_lora_sampler_487
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 1
common_nodes: [BasicScheduler, CLIPLoader, CLIPVisionLoader, CS-MultiImageLoader, ComfyNumberConvert, DiffusionModelLoaderKJ, ImageResizeKJv2, Int, KSamplerSelect, LoraLoaderModelOnly, ModelSamplingSD3, SCAIL2ScheduledLongVideoWithSAM, SCAIL2SegmentPlanBuilder, SimpleMath+, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Scail2-人物替换+多图参考+内循环长视频+人物重打光_2077553871869800449.json, 平台全量/Scail2-人物替换+多图参考+内循环长视频+脸部修复+重打光_2077549370983149570.json, 平台全量/Scail2-人物替换+多图参考+内循环长视频+脸部修复_2073048757691834369.json, 平台全量/Scail2-人物替换+多图参考+内循环长视频_2073033544292716546.json, 平台全量/Scail2-动作迁移+多图参考+内循环长视频+脸部修复_2073220441178730497.json, 平台全量/Scail2-动作迁移+多图参考+内循环长视频_2072661101212422146.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_487

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Scail2-人物替换+多图参考+内循环长视频+人物重打光_2077553871869800449.json、平台全量/Scail2-人物替换+多图参考+内循环长视频+脸部修复+重打光_2077549370983149570.json、平台全量/Scail2-人物替换+多图参考+内循环长视频+脸部修复_2073048757691834369.json、平台全量/Scail2-人物替换+多图参考+内循环长视频_2073033544292716546.json、平台全量/Scail2-动作迁移+多图参考+内循环长视频+脸部修复_2073220441178730497.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPVisionLoader`
- `CS-MultiImageLoader`
- `ComfyNumberConvert`
- `DiffusionModelLoaderKJ`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SCAIL2ScheduledLongVideoWithSAM`
- `SCAIL2SegmentPlanBuilder`
- `SimpleMath+`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 5/6 个有
- `CheckpointLoaderSimple` —— 5/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `GetImageSize` —— 3/6 个有
- `SCAIL2AlignReferenceFaceToCrop` —— 3/6 个有
- `SCAIL2FaceCompositeBack` —— 3/6 个有
- `SCAIL2HeadTrackCrop` —— 3/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
