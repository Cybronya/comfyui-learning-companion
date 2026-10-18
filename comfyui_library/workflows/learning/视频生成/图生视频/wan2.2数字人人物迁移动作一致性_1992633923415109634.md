---
key: 视频生成/图生视频/wan2.2数字人人物迁移动作一致性_1992633923415109634.json
name: wan2.2数字人人物迁移动作一致性_1992633923415109634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2数字人人物迁移动作一致性_1992633923415109634.json
hash: e26f93e497080cd1
coverage: 0.692308
learned_at: 2026-10-15 22:33:16
nodes: [easy cleanGpuUsed, Reroute, Primitive integer [Crystools], AddLabel, RH_Captioner, ImpactSwitch, SetNode, SimpleMath+, SimpleMath+, SetNode, VHS_VideoCombine, RH_Captioner, ImpactSwitch, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], SetNode, GetImageSizeAndCount, WanVideoExperimentalArgs, GetNode, AddLabel, GetNode, WanVideoDecode, EmptyImage, Text Concatenate, GetNode, WanVideoTeaCache, GetNode, GetNode, WanVideoTextEncode, SetNode, GetNode, SetNode, VHS_VideoCombine, Reroute, GetNode, SetNode, WanVideoSLG, WanVideoVAELoader, Text Multiline, Primitive integer [Crystools], SimpleMath+, Primitive integer [Crystools], ImpactSwitch, Text Multiline, easy seed, ImageConcatMulti, RHHiddenNodes, AIO_Preprocessor, Primitive integer [Crystools], WanVideoSampler, Primitive integer [Crystools], RHHiddenNodes, VHS_LoadVideo, LoadImage, LoadWanVideoT5TextEncoder, ShowText|pysssss, ImageConcatMulti, ColorMatch, RHHiddenNodes, GetImageSizeAndCount, WanVideoVACEEncode, ImageResizeKJ, ImageResizeKJ, PreviewImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2数字人人物迁移动作一致性_1992633923415109634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992633923415109634.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（65 个）：
- `easy cleanGpuUsed`
- `Reroute`
- `Primitive integer [Crystools]`
- `AddLabel`
- `RH_Captioner`
- `ImpactSwitch`
- `SetNode`
- `SimpleMath+`
- `SimpleMath+`
- `SetNode`
- `VHS_VideoCombine`
- `RH_Captioner`
- `ImpactSwitch`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoExperimentalArgs`
- `GetNode`
- `AddLabel`
- `GetNode`
- `WanVideoDecode`
- `EmptyImage`
- `Text Concatenate`
- `GetNode`
- `WanVideoTeaCache`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `SetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `Reroute`
- `GetNode`
- `SetNode`
- `WanVideoSLG`
- `WanVideoVAELoader`
- `Text Multiline`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `ImpactSwitch`
- `Text Multiline`
- `easy seed`
- `ImageConcatMulti`
- `RHHiddenNodes`
- `AIO_Preprocessor`
- `Primitive integer [Crystools]`
- `WanVideoSampler` ★核心
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `VHS_LoadVideo`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `ShowText|pysssss`
- `ImageConcatMulti`
- `ColorMatch`
- `RHHiddenNodes`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `PreviewImage`

## 知识

覆盖率 **69%**（45/65）

**有卡**：`easy cleanGpuUsed`、`Primitive integer [Crystools]`、`AddLabel`、`RH_Captioner`、`SimpleMath+`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`EmptyImage`、`Text Concatenate`、`WanVideoTeaCache`、`WanVideoTextEncode`、`WanVideoSLG`、`WanVideoVAELoader`、`Text Multiline`、`easy seed`、`ImageConcatMulti`、`RHHiddenNodes`、`AIO_Preprocessor`、`WanVideoSampler`、`VHS_LoadVideo`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`ColorMatch`、`WanVideoVACEEncode`、`ImageResizeKJ`

**用到的条目**：LoadImage、WanVideoSampler、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode
