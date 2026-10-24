---
name: unknown_workflow_video_lora_sampler_103
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.996133
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, INTConstant, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, Text Concatenate, UNETLoader, VAELoader, VHS_VideoCombine, Wan22PromptSelector, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/实测好用！图生视频，小幅度巨好用_2080827285132898306.json, 视频生成/图生视频/数字人动作，服装，动态展示 Wan2.2 Remix V3 图生视频超流畅最强版_2079587652592037890.json, 视频生成/图生视频/最强 Wan2.2 Remix V3 图生视频｜丝滑流畅升级版_2087862856862748674.json, 视频生成/图生视频/最新图生视频 Wan Remix-V3+人物表情及运镜方式+光线类型 智能焦距_2035900370236481538.json, 视频生成/图生视频/极速生成-图生视频-Wan2.2 Remix V3_2064528658047520769.json, 视频生成/图生视频/超丝滑版图生视频+内置免费的全能图片+高清插帧_2072282561220530178.json, 视频生成/图生视频/返回 Wan2.2 Remix V3 图生视频_2066038287848001538.json, 视频生成/图生视频/返回 Wan2.2 Remix V3 图生视频_极度丝滑没有之一 akcope_2065021049787469825.json, 视频生成/文生视频/Remix-V3  图生视频+人物表情及运镜方式+光线类型 智能焦距_2035184722933977090.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频_2064528430519115778.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频_2064548764462964737.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频_2070034805030477826.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频超流畅最强版_2095030298126929921.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频超流畅最强版_2095807107621801985.json, 视频生成/文生视频/Wan2.2 Remix V3 图生视频超流畅最强版_2104826544370839553.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_103

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/实测好用！图生视频，小幅度巨好用_2080827285132898306.json、视频生成/图生视频/数字人动作，服装，动态展示 Wan2.2 Remix V3 图生视频超流畅最强版_2079587652592037890.json、视频生成/图生视频/最强 Wan2.2 Remix V3 图生视频｜丝滑流畅升级版_2087862856862748674.json、视频生成/图生视频/最新图生视频 Wan Remix-V3+人物表情及运镜方式+光线类型 智能焦距_2035900370236481538.json、视频生成/图生视频/极速生成-图生视频-Wan2.2 Remix V3_2064528658047520769.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `Text Concatenate`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 14/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/15 个有
- `easy cleanGpuUsed` —— 13/15 个有
- `ImageScaleBy` —— 12/15 个有
- `RIFE VFI` —— 12/15 个有
- `ImageResizeKJv2` —— 2/15 个有
- `JjkText` —— 1/15 个有
- `LoadAudio` —— 1/15 个有
- `PreviewImage` —— 1/15 个有
- `RHHiddenNodes` —— 1/15 个有
- `SaveImage` —— 1/15 个有
- `VAEDecodeTiled` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 15 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 15 | 100% |
| 采样算法 | 1 | 1 - 1 | 15 | 100% |
| 调度器 | euler | - | 15 | 100% |
| 重绘幅度 | simple | - | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，15 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，15 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，15 个样本，一致性 100%
- 重绘幅度 最常用 simple，15 个样本，一致性 100%
