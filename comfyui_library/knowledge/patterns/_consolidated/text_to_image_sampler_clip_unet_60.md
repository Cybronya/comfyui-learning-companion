---
name: text_to_image_sampler_clip_unet_60
type: Text To Image
frequency: 10
level: moderate
coverage: 0.8158
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, KSampler, PreviewAny, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/图生图/Anima base 动漫图片编辑，可指定画师-AIGC大赏_2064637242760581122.json, 图片生成/图生图/最强动漫 Anima base v1.0 图生图 提示词扩写 自动匹配画师_2056557560999792641.json, 图片生成/图生图/最强动漫模型 Anima3 图生图 带提示词扩写 可自动匹配画师_2045329775052460034.json, 图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2057631235354226689.json, 图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2058751293228933122.json, 图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json, 图片生成/文生图/Anima3 动漫文生图 qwen3.5提示词优化，可指定画师风格_2045768388223438850.json, 图片生成/文生图/动漫-文生图-提示词扩写-自动匹配画师_2057343678515073025.json, 图片生成/文生图/最强动漫 Anima base v1.0 文生图 提示词扩写 自动匹配画师_2056541097979109378.json, 图片生成/文生图/最强动漫模型 Anima3 文生图 带提示词扩写 可自动匹配画师_2044417404951863297.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Anima base 动漫图片编辑，可指定画师-AIGC大赏_2064637242760581122.json、图片生成/图生图/最强动漫 Anima base v1.0 图生图 提示词扩写 自动匹配画师_2056557560999792641.json、图片生成/图生图/最强动漫模型 Anima3 图生图 带提示词扩写 可自动匹配画师_2045329775052460034.json、图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2057631235354226689.json、图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2058751293228933122.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 9/10 个有
- `LayerUtility: ImageReel` —— 7/10 个有
- `LayerUtility: ImageReelComposit` —— 7/10 个有
- `Seed_` —— 7/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `LoadImage` —— 3/10 个有
- `SeedVR2LoadDiTModel` —— 3/10 个有
- `SeedVR2LoadVAEModel` —— 3/10 个有
- `SeedVR2VideoUpscaler` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `CompressImages` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `Int` —— 1/10 个有
- `ZML_AnyTypeSwitchFive` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 35 | 10 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 10 | 33% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1536 | 896 - 1536 | 10 | 78% |
| 高度 | 1536 | 1152 - 1536 | 10 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 35，10 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，10 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 896 - 1536，10 个样本
- 高度 中位数 1536，观测区间 1152 - 1536，10 个样本，取值集中（一致性 88%）
