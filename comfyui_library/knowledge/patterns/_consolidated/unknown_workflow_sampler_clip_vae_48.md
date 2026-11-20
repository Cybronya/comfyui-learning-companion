---
name: unknown_workflow_sampler_clip_vae_48
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9182
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, Get Image Size, InFluxModelSamplingPred, Joy_caption_two, Joy_caption_two_load, LoadImage, OutFluxModelSamplingPred, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/产品精修工作流 （可选多材质精修）_2003658762684669953.json, 图片生成/图生图/精修去褶皱工作流 服装、箱包、帆布袋适用 flux逆采样工作流_1933120693514973186.json, 平台全量/flux1版 基础电商产品精修  2026.1.18更新_1964153515574743042.json, 平台全量/rfinversion逆采样产品精修_1928629572710076417.json, 平台全量/【服饰精修】提取服饰精修 精修去褶皱  服装、箱包、帆布袋适用_1989578191075463169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_48

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/产品精修工作流 （可选多材质精修）_2003658762684669953.json、图片生成/图生图/精修去褶皱工作流 服装、箱包、帆布袋适用 flux逆采样工作流_1933120693514973186.json、平台全量/flux1版 基础电商产品精修  2026.1.18更新_1964153515574743042.json、平台全量/rfinversion逆采样产品精修_1928629572710076417.json、平台全量/【服饰精修】提取服饰精修 精修去褶皱  服装、箱包、帆布袋适用_1989578191075463169.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `Get Image Size`
- `InFluxModelSamplingPred`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `LoadImage`
- `OutFluxModelSamplingPred`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `NunchakuFluxDiTLoader` —— 4/5 个有
- `ConstrainImage|pysssss` —— 3/5 个有
- `DualCLIPLoader` —— 3/5 个有
- `ImageUpscaleWithModel` —— 3/5 个有
- `Upscale Model Loader` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 2/5 个有
- `ImageScale` —— 2/5 个有
- `Int` —— 2/5 个有
- `NunchakuFluxLoraLoader` —— 2/5 个有
- `NunchakuTextEncoderLoader` —— 2/5 个有
- `LoraLoader` —— 1/5 个有
- `UNETLoader` —— 1/5 个有
- `easy clearCacheAll` —— 1/5 个有
- `easy showAnythingLazy` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
