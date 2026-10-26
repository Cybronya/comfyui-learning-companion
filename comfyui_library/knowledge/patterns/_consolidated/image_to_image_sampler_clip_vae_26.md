---
name: image_to_image_sampler_clip_vae_26
type: Image To Image
frequency: 8
level: strong
coverage: 0.92075
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux Kontext超强去水印（numchaku10倍加速）_1941322884021383170.json, 图片生成/图生图/Flux kontext dev（三图版）极速电商万能融合王 指定动作换装换商品换背景_1945397369816981506.json, 图片生成/图生图/Flux-Kontext-Dev单图编辑极速工作流_1938581341325680641.json, 图片生成/图生图/KONTEXT超级美颜，逼真皮肤纹理_1948333109749121025.json, 图片生成/图生图/Kontext抖音图文快速版_1942169548500135937.json, 图片生成/图生图/Kontext（3D透明玻璃材质）_1946032275093942274.json, 图片生成/图生图/Kontext（国风刺绣风格）_1948667825243205633.json, 图片生成/图生图/毛线风格（Kontext Lora）_1949405488208326657.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_26

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux Kontext超强去水印（numchaku10倍加速）_1941322884021383170.json、图片生成/图生图/Flux kontext dev（三图版）极速电商万能融合王 指定动作换装换商品换背景_1945397369816981506.json、图片生成/图生图/Flux-Kontext-Dev单图编辑极速工作流_1938581341325680641.json、图片生成/图生图/KONTEXT超级美颜，逼真皮肤纹理_1948333109749121025.json、图片生成/图生图/Kontext抖音图文快速版_1942169548500135937.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 6/8 个有
- `EmptySD3LatentImage` —— 5/8 个有
- `TeaCache` —— 5/8 个有
- `UNETLoader` —— 5/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `LayerUtility: ImageReel` —— 3/8 个有
- `LayerUtility: ImageReelComposit` —— 3/8 个有
- `LoadImageOutput` —— 3/8 个有
- `NunchakuFluxDiTLoader` —— 3/8 个有
- `RH_Translator` —— 3/8 个有
- `Bjornulf_ShowStringText` —— 2/8 个有
- `CR Text` —— 2/8 个有
- `ImpactSwitch` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `CR Simple Image Compare` —— 1/8 个有
- `ImageUpscaleWithModel` —— 1/8 个有
- `RepeatLatentBatch` —— 1/8 个有
- `UpscaleModelLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 8 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
