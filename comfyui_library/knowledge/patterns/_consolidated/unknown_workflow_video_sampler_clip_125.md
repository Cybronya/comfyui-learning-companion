---
name: unknown_workflow_video_sampler_clip_125
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7758
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), GetNode, INTConstant, KSamplerAdvanced, LoadImage, ModelSamplingSD3, Seed (rgthree), SetNode, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/DASIWA VBVR逻辑推理强化工作流_2029377016692219906.json, 视频生成/图生视频/Wan2.2 Remix i2v 2.1 图生视频VBVR逻辑推理强化工作流_2027033853302411266.json, 视频生成/图生视频/Wan2.2 Remix i2v 3.0 图生视频_2036411517872119810.json, 视频生成/图生视频/Wan2.2+Remix+图生视频VBVR逻辑推理强化工作流_2036279680805900289.json, 视频生成/图生视频/Wan2.2图生视频_2036392422615293954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_125

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/DASIWA VBVR逻辑推理强化工作流_2029377016692219906.json、视频生成/图生视频/Wan2.2 Remix i2v 2.1 图生视频VBVR逻辑推理强化工作流_2027033853302411266.json、视频生成/图生视频/Wan2.2 Remix i2v 3.0 图生视频_2036411517872119810.json、视频生成/图生视频/Wan2.2+Remix+图生视频VBVR逻辑推理强化工作流_2036279680805900289.json、视频生成/图生视频/Wan2.2图生视频_2036392422615293954.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `Seed (rgthree)`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 4/5 个有
- `JjkText` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `llama_cpp_instruct_adv` —— 3/5 个有
- `llama_cpp_model_loader` —— 3/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `LayerUtility: TextJoin` —— 2/5 个有
- `ModelPatchTorchSettings` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `TextInput_` —— 2/5 个有
- `CR Text` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `PainterVRAM` —— 1/5 个有
- `Switch any [Crystools]` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 80%
