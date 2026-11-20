---
name: unknown_workflow_video_lora_sampler_133
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.669333
common_nodes: [GetImageRangeFromBatch, GrowMask, ImageResizeKJv2, LoadImage, MochaEmbeds, PointsEditor, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader, easy imageRemBg]
problems: []
missing: []
members: [平台全量/Mocha视频人物替换_1981140638525689857.json, 平台全量/Mocha角色替换工作流_2049685591721299970.json, 平台全量/Mocha角色替换工作流_2052227583365918721.json, 平台全量/【角色替换】Mocha工作流_1982702781029064706.json, 平台全量/人物替换Mocha工作流Wan（支持10s以上）_1980855771195985922.json, 平台全量/视频人物替换_1981139819441045506.json, 平台全量/角色替换Mocha工作流_1980672974778974209.json, 平台全量/角色替换Mocha工作流_1992915717536366593.json, 数字人/数字人/图片生成  全能视频 人物替换Mocha 【如爆显存 请使用 Plus模式】 数字人说话唱歌跳_2064208363466092546.json, 视频生成/图生视频/Mocha sec4b视频抠图工作流_1982464273806966785.json, 视频生成/图生视频/人物替换Mocha工作流Wan（支持10s以上）_2013864867756773377.json, 视频生成/图生视频/最新视频角色替换Mocha_1980911162026016770.json, 视频生成/图生视频/角色替换Mocha_1980827522109755393.json, 视频生成/图生视频/角色替换Mocha工作流_1986007241096605697.json, 视频生成/图生视频/🦖Mocha角色替换_1980895212593659906.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_133

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（平台全量/Mocha视频人物替换_1981140638525689857.json、平台全量/Mocha角色替换工作流_2049685591721299970.json、平台全量/Mocha角色替换工作流_2052227583365918721.json、平台全量/【角色替换】Mocha工作流_1982702781029064706.json、平台全量/人物替换Mocha工作流Wan（支持10s以上）_1980855771195985922.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 15 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GrowMask`
- `ImageResizeKJv2`
- `LoadImage`
- `MochaEmbeds`
- `PointsEditor`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 14/15 个有
- `MaskPreview` —— 14/15 个有
- `PreviewImage` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `WanVideoTorchCompileSettings` —— 14/15 个有
- `ImageConcanate` —— 13/15 个有
- `Int` —— 5/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/15 个有
- `DF_Int_to_Float` —— 3/15 个有
- `MathExpression|pysssss` —— 3/15 个有
- `RMBG` —— 3/15 个有
- `SimpleMath+` —— 2/15 个有
- `ACE_ImageFaceCrop` —— 1/15 个有
- `DeepTranslatorTextNode` —— 1/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `Fast Groups Muter (rgthree)` —— 1/15 个有
- `FlashVSRNode` —— 1/15 个有
- `INTConstant` —— 1/15 个有
- `MaskPreview+` —— 1/15 个有
- `VHS_VideoInfoLoaded` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
