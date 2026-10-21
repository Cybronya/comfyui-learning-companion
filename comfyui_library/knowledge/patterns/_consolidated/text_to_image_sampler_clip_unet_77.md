---
name: text_to_image_sampler_clip_unet_77
type: Text To Image
frequency: 6
level: moderate
coverage: 0.824833
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, KSampler, PreviewAny, Seed_, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2057631235354226689.json, 图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2058751293228933122.json, 图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json, 图片生成/文生图/Anima base 动漫文生图，可指定画师-AIGC大赏_2064644644515966978.json, 图片生成/文生图/动漫-文生图-提示词扩写-自动匹配画师_2057343678515073025.json, 图片生成/文生图/最强动漫 Anima base v1.0 文生图 提示词扩写 自动匹配画师_2056541097979109378.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2057631235354226689.json、图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2058751293228933122.json、图片生成/文生图/Anima base v1.0 文生图 提示词扩写 自动匹配画师_2100427692003913729.json、图片生成/文生图/Anima base 动漫文生图，可指定画师-AIGC大赏_2064644644515966978.json、图片生成/文生图/动漫-文生图-提示词扩写-自动匹配画师_2057343678515073025.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `Seed_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 5/6 个有
- `LayerUtility: ImageReelComposit` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `CompressImages` —— 1/6 个有
- `ShellAgentPluginOutputText` —— 1/6 个有
- `YANC.ConcatStrings` —— 1/6 个有
- `easy imageToBase64` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 35 | 6 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1536 | 864 - 1536 | 6 | 82% |
| 高度 | 1536 | 1536 - 1536 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 35，6 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 864 - 1536，6 个样本，取值集中（一致性 82%）
- 高度 中位数 1536，观测区间 1536 - 1536，6 个样本，取值集中（一致性 100%）
