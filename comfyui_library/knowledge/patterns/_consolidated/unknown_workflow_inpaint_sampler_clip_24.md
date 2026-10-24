---
name: unknown_workflow_inpaint_sampler_clip_24
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9342
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX高清扩图_1959111581642731522.json, 图片生成/图生图/Flux fill One Reward 完美扩图 teacache 加速版_1966425847697747969.json, 图片生成/图生图/OneReward 精准扩图重绘_1967621188161855490.json, 图片生成/图生图/扩图 工作流 还原风格_1985910968855273474.json, 图片生成/图生图/新版好用的扩图流Fill-OneReward-_1981658380387393538.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX高清扩图_1959111581642731522.json、图片生成/图生图/Flux fill One Reward 完美扩图 teacache 加速版_1966425847697747969.json、图片生成/图生图/OneReward 精准扩图重绘_1967621188161855490.json、图片生成/图生图/扩图 工作流 还原风格_1985910968855273474.json、图片生成/图生图/新版好用的扩图流Fill-OneReward-_1981658380387393538.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 4/5 个有
- `ImagePadForOutpaint` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `RH_Translator` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `MaskPreview+` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `ImageCompositeMasked` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImagePadKJ` —— 1/5 个有
- `ImageScaleDownToSize` —— 1/5 个有
- `TeaCache` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 22 | 5 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | normal | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 22，5 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 normal，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
