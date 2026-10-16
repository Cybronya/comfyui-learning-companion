---
key: 视频生成/图生视频/WAN2.1图生视频 _WanI2V-  By Sam（作者）_1901190915296501761.json
name: WAN2.1图生视频 _WanI2V-  By Sam（作者）_1901190915296501761.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1901190915296501761.json
hash: 604d38c2fc5dbd89
coverage: 0.847826
learned_at: 2026-10-15 22:29:23
nodes: [Int To Number (mtb), Number Multiple Of, Number to Int, Int To Number (mtb), Number Multiple Of, Number to Int, GetImageSizeAndCount, JWImageResizeByLongerSide, Context (rgthree), ImageScale, easy imageSize, SamplerCustom, INTConstant, CLIPVisionEncode, Context (rgthree), DF_Logic_node, INTConstant, SplitSigmas, KSamplerSelect, WanImageToVideo, SamplerCustom, CLIPTextEncode, VHS_VideoCombine, MathExpression|pysssss, MathExpression|pysssss, BasicScheduler, UnetLoaderGGUF, UNETLoader, VAELoader, CLIPLoader, CLIPVisionLoader, LoadImage, INTConstant, Power Lora Loader (rgthree), Display Any (rgthree), Note, Label (rgthree), VAEDecodeTiled, Note, Note, Note, Note, Note, Note, SaveAnimatedWEBP, CLIPTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1图生视频 _WanI2V-  By Sam（作者）_1901190915296501761.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1901190915296501761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `Int To Number (mtb)`
- `Number Multiple Of`
- `Number to Int`
- `Int To Number (mtb)`
- `Number Multiple Of`
- `Number to Int`
- `GetImageSizeAndCount`
- `JWImageResizeByLongerSide`
- `Context (rgthree)`
- `ImageScale`
- `easy imageSize`
- `SamplerCustom` ★核心
- `INTConstant`
- `CLIPVisionEncode`
- `Context (rgthree)`
- `DF_Logic_node`
- `INTConstant`
- `SplitSigmas`
- `KSamplerSelect` ★核心
- `WanImageToVideo`
- `SamplerCustom` ★核心
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `BasicScheduler`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPVisionLoader`
- `LoadImage`
- `INTConstant`
- `Power Lora Loader (rgthree)`
- `Display Any (rgthree)`
- `Note`
- `Label (rgthree)`
- `VAEDecodeTiled` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `SaveAnimatedWEBP`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **85%**（39/46）

**有卡**：`Int To Number (mtb)`、`Number Multiple Of`、`Number to Int`、`GetImageSizeAndCount`、`JWImageResizeByLongerSide`、`Context (rgthree)`、`ImageScale`、`easy imageSize`、`SamplerCustom`、`INTConstant`、`CLIPVisionEncode`、`DF_Logic_node`、`SplitSigmas`、`KSamplerSelect`、`WanImageToVideo`、`CLIPTextEncode`、`VHS_VideoCombine`、`MathExpression|pysssss`、`BasicScheduler`、`UnetLoaderGGUF`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`LoadImage`、`Power Lora Loader (rgthree)`、`Display Any (rgthree)`、`Label (rgthree)`、`VAEDecodeTiled`、`SaveAnimatedWEBP`

**用到的条目**：VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom、VAEDecodeTiled
