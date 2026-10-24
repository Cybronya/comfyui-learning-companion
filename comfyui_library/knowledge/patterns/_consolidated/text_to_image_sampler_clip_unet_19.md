---
name: text_to_image_sampler_clip_unet_19
type: Text To Image
frequency: 17
level: weak
coverage: 0.897
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2基础图生图（图像反推提示词）_2070531152993153026.json, 图片生成/文生图/Krea2 文生图_2096503316002983938.json, 图片生成/文生图/Krea2 文生图｜简洁好用出图稳定的新选择_2096849879007059970.json, 图片生成/文生图/Krea2-全能一键出神图文生图2K直出-MJ平替_2070119686372675586.json, 图片生成/文生图/Krea2-全能一键出神图文生图2K直出-MJ平替_2083146964568469505.json, 图片生成/文生图/Krea2-全能一键出神图文生图2K直出-MJ平替工作流_2070135569459539969.json, 图片生成/文生图/Krea2-全能文生图2K直出-MJ平替_2069630824286347266.json, 图片生成/文生图/Krea2-全能文生图2K直出-MJ平替_2073595533018808320.json, 图片生成/文生图/Krea2-全能文生图2K直出-MJ平替_2096072679521603585.json, 图片生成/文生图/Krea2-全能文生图2K直出-油画风格_2079461576461086722.json, 图片生成/文生图/Krea2-文生图（ Kroma完整还原原版微调模型能力）_2083852283707748353.json, 图片生成/文生图/Krea2-文生图（写实增强）2K直出_2076180135027499010.json, 图片生成/文生图/Krea2全能文生图2K直出｜MJ平替高质量图像生成_2096319734013845505.json, 图片生成/文生图/Krea2全能文生图简单版_2096511693064065026.json, 图片生成/文生图/Krea2模型文生图工作流，高质量文本到图像生成方案_2102885318025371650.json, 图片生成/文生图/Krea2模型文生图工作流，高质量文本到图像生成方案_2105111992758530050.json, 图片生成/文生图/两K直出不缩水｜Krea2全能文生图MJ平替_2096585844239982594.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_19

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Krea2基础图生图（图像反推提示词）_2070531152993153026.json、图片生成/文生图/Krea2 文生图_2096503316002983938.json、图片生成/文生图/Krea2 文生图｜简洁好用出图稳定的新选择_2096849879007059970.json、图片生成/文生图/Krea2-全能一键出神图文生图2K直出-MJ平替_2070119686372675586.json、图片生成/文生图/Krea2-全能一键出神图文生图2K直出-MJ平替_2083146964568469505.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 16/17 个有
- `LoraLoaderModelOnly` —— 16/17 个有
- `PreviewAny` —— 16/17 个有
- `easy cleanGpuUsed` —— 16/17 个有
- `TTResolutionSelector` —— 11/17 个有
- `DF_Latent_Scale_to_side` —— 6/17 个有
- `JjkText` —— 6/17 个有
- `ResolutionSelector` —— 6/17 个有
- `solarL_SaveImagesToZip` —— 6/17 个有
- `孤海注释` —— 4/17 个有
- `CR Text Concatenate` —— 1/17 个有
- `EmptyImage` —— 1/17 个有
- `LoadImage` —— 1/17 个有
- `MuyeTextEditOutput` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `StringConcatenate` —— 1/17 个有
- `easy showAnything` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 512 | 17 | 49% |
| 高度 | 512 | 80 - 512 | 17 | 49% |
| 采样步数 | 8 | 4 - 8 | 17 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 17 | 21% |
| 采样算法 | er_sde | - | 17 | 94% |
| 调度器 | simple | - | 17 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 512，17 个样本，取值分散，一致性仅 49%
- 高度 中位数 512，观测区间 80 - 512，17 个样本，取值分散，一致性仅 49%
- 采样步数 中位数 8，观测区间 4 - 8，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，17 个样本，取值分散，一致性仅 21%
- 采样算法 最常用 er_sde，17 个样本，一致性 94%
- 调度器 最常用 simple，17 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 高发问题（23/17 个样本）：Steps较低可能导致细节不足
