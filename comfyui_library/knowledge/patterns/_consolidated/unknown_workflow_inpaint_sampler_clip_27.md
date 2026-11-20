---
name: unknown_workflow_inpaint_sampler_clip_27
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.931143
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX高清扩图_1959111581642731522.json, 图片生成/图生图/Flux fill One Reward 完美扩图 teacache 加速版_1966425847697747969.json, 图片生成/图生图/OneReward 精准扩图重绘_1967621188161855490.json, 图片生成/图生图/扩图 工作流 还原风格_1985910968855273474.json, 图片生成/图生图/新版好用的扩图流Fill-OneReward-_1981658380387393538.json, 平台全量/Fill-OneReward-新版好用的扩图流_1968572218340986881.json, 平台全量/消除水印_1873731016245559298.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/FLUX高清扩图_1959111581642731522.json、图片生成/图生图/Flux fill One Reward 完美扩图 teacache 加速版_1966425847697747969.json、图片生成/图生图/OneReward 精准扩图重绘_1967621188161855490.json、图片生成/图生图/扩图 工作流 还原风格_1985910968855273474.json、图片生成/图生图/新版好用的扩图流Fill-OneReward-_1981658380387393538.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
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
- `GrowMaskWithBlur` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `ConditioningZeroOut` —— 5/7 个有
- `ImagePadForOutpaint` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/7 个有
- `MaskPreview+` —— 5/7 个有
- `RH_Translator` —— 5/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `ImageCompositeMasked` —— 2/7 个有
- `Image Overlay` —— 1/7 个有
- `ImagePadKJ` —— 1/7 个有
- `ImageScaleDownToSize` —— 1/7 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/7 个有
- `TeaCache` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 22 | 7 | 97% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | beta | - | 7 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 22，7 个样本，取值集中（一致性 97%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
