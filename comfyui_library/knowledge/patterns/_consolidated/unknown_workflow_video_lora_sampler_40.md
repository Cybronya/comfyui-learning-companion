---
name: unknown_workflow_video_lora_sampler_40
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.498778
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, DiffusionModelLoaderKJ, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [图片生成/图生图/Scail2视频角色替换又快又好_2065296557842460673.json, 图片生成/图生图/【遇见AI】wan2.1 SCAIL2 角色替换 动作迁移 姿势参考_2065988482132168705.json, 图片生成/图生图/余温人物替换工作流（麦田动漫工作室专享）_2114727210098708481.json, 图片生成/图生图/余温动作迁移工作流（麦田动漫工作室专享）_2114725338843537409.json, 图片生成/图生图/余温｜麦田动漫工作室专属的人物替换视频换脸处理工作流_2114619410991378434.json, 图片生成/图生图/余温｜麦田动漫工作室专属的动作迁移加视频换背景换脸工作流_2114617576302145537.json, 图片生成/图生图/全新动作模仿 SCAIL2！单人or双人（懒人版）_2066568712282525697.json, 平台全量/SCAIL 2单人_双人动作迁移（二次采样版）2606_2065754332263440385.json, 平台全量/SCAIL2  实测好用—高动态视频精准模仿 动作迁移 姿态模仿 单人精准版_2070493724886519809.json, 平台全量/Scail2完美人物替换工作流_2068582534954442754.json, 平台全量/Scail2视频角色替换_2069649445913980930.json, 平台全量/Scail2角色替换_2069645906240163842.json, 平台全量/余温人物替换工作流（麦田动漫工作室专享）_2106912987813601282.json, 平台全量/余温动作迁移工作流（麦田动漫工作室专享）_2107501186487242753.json, 平台全量/全新动作模仿 SCAIL2_2067261252719702018.json, 平台全量/全新动作模仿 SCAIL2！单人or双人！B站艾橘溪_2065827947965149186.json, 平台全量/实用版本的个人Scail2循环动作迁移_2119021926776655873.json, 平台全量/最新Scail2!动作迁移_人物替换！_2065239580168769538.json, 平台全量/最新Scail2!动作迁移_人物替换！_2067407197683937281.json, 视频生成/图生视频/SCAIL2全新单双人动作模仿_2065273822449856514.json, 视频生成/图生视频/SCAIL2双人+单人角色替换！视频换人_2067601389454454786.json, 视频生成/图生视频/SCAIL2双人+单人角色替换！视频换人_2067602340542246914.json, 视频生成/图生视频/SCAIL2视频单双人动作模仿_2065718753207349250.json, 视频生成/图生视频/全新动作模仿 SCAIL2_2066834222895161346.json, 视频生成/图生视频/全新动作模仿 SCAIL2！单人or双人（懒人版）_2067171226954584065.json, 视频生成/图生视频/全新走路跳舞动作模仿迁移复制转移 SCAIL2！单人or双人（懒人版）_2069078995290906625.json, 视频生成/图生视频/动作迁移 双人_单人视频换人 角色替换SCAIL2_2066697586874085378.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_40

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/Scail2视频角色替换又快又好_2065296557842460673.json、图片生成/图生图/【遇见AI】wan2.1 SCAIL2 角色替换 动作迁移 姿势参考_2065988482132168705.json、图片生成/图生图/余温人物替换工作流（麦田动漫工作室专享）_2114727210098708481.json、图片生成/图生图/余温动作迁移工作流（麦田动漫工作室专享）_2114725338843537409.json、图片生成/图生图/余温｜麦田动漫工作室专属的人物替换视频换脸处理工作流_2114619410991378434.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DiffusionModelLoaderKJ`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `ColorTransfer` —— 26/27 个有
- `GetImageRangeFromBatch` —— 26/27 个有
- `WanChunkFeedForward` —— 25/27 个有
- `GetNode` —— 23/27 个有
- `SetNode` —— 23/27 个有
- `ImageConcatMulti` —— 22/27 个有
- `PreviewImage` —— 21/27 个有
- `PreviewAny` —— 19/27 个有
- `PrimitiveInt` —— 19/27 个有
- `ImageFromBatch` —— 18/27 个有
- `SimpleMath+` —— 18/27 个有
- `ttN int` —— 18/27 个有
- `easy cleanGpuUsed` —— 15/27 个有
- `JjkText` —— 13/27 个有
- `Seed` —— 12/27 个有
- `AILab_QwenVL` —— 9/27 个有
- `easy imageRemBg` —— 8/27 个有
- `INTConstant` —— 7/27 个有
- `LayerMask: RemBgUltra` —— 7/27 个有
- `SaveVideoNode` —— 7/27 个有
- `ShowText|pysssss` —— 6/27 个有
- `InversionDemoLazySwitch` —— 3/27 个有
- `PrimitiveBoolean` —— 3/27 个有
- `Label (rgthree)` —— 2/27 个有
- `孤海注释` —— 2/27 个有
- `ComfyMathExpression` —— 1/27 个有
- `FlashVSRInitPipe` —— 1/27 个有
- `FlashVSRNodeAdv` —— 1/27 个有
- `GetImageSize` —— 1/27 个有
- `TensorLoopClose` —— 1/27 个有
- `TensorLoopOpen` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
