---
name: unknown_workflow_video_sampler_vae_14
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.942222
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1933536607737921538.json, 视频生成/图生视频/1934652998628876289.json, 视频生成/图生视频/2059216545439637505.json, 视频生成/图生视频/2059998654034964482.json, 视频生成/图生视频/2059999061939408898.json, 视频生成/图生视频/2081413753370931202.json, 视频生成/图生视频/LORA版本-FusionX+VACE图生视频_2084126269507198978.json, 视频生成/图生视频/LORA版本-FusionX+VACE图生视频_2084278181875507201.json, 视频生成/图生视频/1935716384242659330.json, 视频生成/图生视频/1933574608002138113.json, 视频生成/图生视频/1933179380589834241.json, 视频生成/图生视频/2050795023934992385.json, 视频生成/图生视频/1935508820678332418.json, 视频生成/图生视频/1990978944960765954.json, 视频生成/文生视频/1950451311817965570.json, 视频生成/文生视频/1950453907279536130.json, 视频生成/文生视频/1950797780040220674.json, 视频生成/文生视频/1934251292992696321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_14

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1933536607737921538.json、视频生成/图生视频/1934652998628876289.json、视频生成/图生视频/2059216545439637505.json、视频生成/图生视频/2059998654034964482.json、视频生成/图生视频/2059999061939408898.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 18 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 17/18 个有
- `ShowText` —— 17/18 个有
- `WanVideoTorchCompileSettings` —— 17/18 个有
- `WanVideoVACEModelSelect` —— 17/18 个有
- `WanVideoLoraSelect` —— 16/18 个有
- `RH_LLMAPI_NODE` —— 14/18 个有
- `WanVideoEnhanceAVideo` —— 14/18 个有
- `WanVideoExperimentalArgs` —— 14/18 个有
- `JWStringReplace` —— 11/18 个有
- `Compare` —— 4/18 个有
- `RH_Captioner` —— 4/18 个有
- `Text Concatenate` —— 4/18 个有
- `Text Multiline (Code Compatible)` —— 4/18 个有
- `easy ifElse` —— 4/18 个有
- `LoadLatent` —— 3/18 个有
- `SaveLatent` —— 3/18 个有
- `String Replace (mtb)` —— 3/18 个有
- `SimpleMath+` —— 1/18 个有
- `WanVideoSLG` —— 1/18 个有
- `WanVideoTeaCache` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
