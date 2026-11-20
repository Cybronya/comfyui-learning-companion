---
name: unknown_workflow_video_sampler_clip_28
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.950937
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImpactInt, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/101.图生视频_2003315240559312897.json, 视频生成/图生视频/Smooth Mix Wan 2.2 超好用的图生视频大模型_1979525930601320449.json, 视频生成/图生视频/YJ-APP-Wan2.2-Smooth-I2V_2038634972579373058.json, 视频生成/图生视频/wan2.2 Smooth Mix V2高动态电影质感 图生视频_2013454725135470593.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1980432616040148994.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1983880606536925186.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2010998394537381889.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2035897809894903809.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2039617670403858433.json, 视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_2041028074229211137.json, 视频生成/图生视频/wan2.2 Smooth Mix 高级电影质感和短剧—— 图生视频_1980633692215361538.json, 视频生成/图生视频/wan2.2 图生视频_2006925723407228930.json, 视频生成/图生视频/图生视频_1986278808032595970.json, 视频生成/图生视频/电影时光机+爆款复刻+多图首尾帧_2007316422707388418.json, 视频生成/图生视频/飞行魔法少女+飞行滑板+多图首尾帧_2006937829007433729.json, 视频生成/图生视频/🚵Smooth Mix wan2.2 高动态电影质感模型 图生视频🚵_1979384591175815170.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/101.图生视频_2003315240559312897.json、视频生成/图生视频/Smooth Mix Wan 2.2 超好用的图生视频大模型_1979525930601320449.json、视频生成/图生视频/YJ-APP-Wan2.2-Smooth-I2V_2038634972579373058.json、视频生成/图生视频/wan2.2 Smooth Mix V2高动态电影质感 图生视频_2013454725135470593.json、视频生成/图生视频/wan2.2 Smooth Mix 高动态电影质感 图生视频_1980432616040148994.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 15/16 个有
- `PrimitiveStringMultiline` —— 15/16 个有
- `Seed (rgthree)` —— 15/16 个有
- `WanImageToVideo` —— 14/16 个有
- `easy cleanGpuUsed` —— 14/16 个有
- `wanBlockSwap` —— 14/16 个有
- `Fast Bypasser (rgthree)` —— 13/16 个有
- `Mute / Bypass Repeater (rgthree)` —— 13/16 个有
- `ImageScaleBy` —— 11/16 个有
- `RIFE VFI` —— 10/16 个有
- `RHHiddenNodes` —— 3/16 个有
- `Text Concatenate` —— 2/16 个有
- `WanAdvancedI2V` —— 2/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `LoraLoaderModelOnly` —— 1/16 个有
- `Note Plus (mtb)` —— 1/16 个有
- `RH_LLMAPI_NODE` —— 1/16 个有
- `RH_Translator` —— 1/16 个有
- `TextInput_` —— 1/16 个有
- `Wan22PromptSelector` —— 1/16 个有
- `easy showAnything` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 16 | 81% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 16 | 100% |
| 采样算法 | 1 | 1 - 1 | 16 | 100% |
| 调度器 | euler_ancestral | - | 16 | 94% |
| 重绘幅度 | simple | - | 16 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，16 个样本，一致性 81%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，16 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，16 个样本，一致性 94%
- 重绘幅度 最常用 simple，16 个样本，一致性 94%
