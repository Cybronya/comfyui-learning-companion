---
name: unknown_workflow_video_sampler_clip_31
type: Unknown Workflow
frequency: 13
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1989613894270414850.json, 视频生成/图生视频/1988980574498992130.json, 视频生成/图生视频/1990058904107274241.json, 视频生成/图生视频/2075187297317908481.json, 视频生成/图生视频/2075871515157024769.json, 视频生成/图生视频/2078365547917570049.json, 视频生成/图生视频/2080463180828078082.json, 视频生成/图生视频/2008211461260189698.json, 视频生成/图生视频/2047195777209999362.json, 视频生成/图生视频/2047212911168327682.json, 视频生成/图生视频/2047468102497079298.json, 视频生成/图生视频/2035900370236481538.json, 视频生成/文生视频/Remix-V3  图生视频+人物表情及运镜方式+光线类型 智能焦距_2035184722933977090.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1989613894270414850.json、视频生成/图生视频/1988980574498992130.json、视频生成/图生视频/1990058904107274241.json、视频生成/图生视频/2075187297317908481.json、视频生成/图生视频/2075871515157024769.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/13 个有
- `ModelPatchTorchSettings` —— 10/13 个有
- `WanFirstMiddleLastFrameToVideo` —— 10/13 个有
- `CR Text` —— 3/13 个有
- `Wan22PromptSelector` —— 3/13 个有
- `CLIPVisionEncode` —— 2/13 个有
- `CLIPVisionLoader` —— 2/13 个有
- `Text Concatenate` —— 2/13 个有
- `WanImageToVideo` —— 2/13 个有
- `ColorMatch_UTK` —— 1/13 个有
- `LayerUtility: TextJoin` —— 1/13 个有
- `PainterI2V` —— 1/13 个有
- `YC Color Match` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 13 | 100% |
| Prompt 约束强度(CFG) | 6 | 4 - 6 | 13 | 91% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | euler | - | 13 | 100% |
| 重绘幅度 | beta | - | 13 | 54% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，13 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 6，13 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，13 个样本，一致性 100%
- 重绘幅度 最常用 beta，13 个样本，一致性 54%
