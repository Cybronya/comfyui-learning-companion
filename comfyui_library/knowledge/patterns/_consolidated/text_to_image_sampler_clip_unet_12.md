---
name: text_to_image_sampler_clip_unet_12
type: Text To Image
frequency: 24
level: weak
coverage: 0.890083
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/krea2+Qwen3.5-自动多风格文生图_2084922609443102721.json, 图片生成/文生图/Anima -aesthetic-v1.1-自动提示词动漫文生图（加速版）_2078097784728805377.json, 图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json, 图片生成/文生图/Krea 2 Text to Image 文生图 (超强写实质感)_2075054887305568258.json, 图片生成/文生图/Krea2美人极速版，支持反推。_2092435948138221569.json, 图片生成/文生图/RedCraft Krea 2 红潮版_2075054152518029314.json, 图片生成/文生图/Zimage 直出真实感网红图片 林耀3.18_2034176377439653889.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2072869610650689537.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084176385911902210.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084180097455710209.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084184981282312193.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084188539746611201.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084191590809165826.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084543653397221377.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084547006332231681.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084566111013662721.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2084568266718142466.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2086317060350631938.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2086324082525696001.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2089597886714699778.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2089606694295924738.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2093221605420916737.json, 图片生成/文生图/krea2+Qwen3.5-自动多风格文生图_2093225496157970434.json, 图片生成/文生图/啊癫z-image 角色资产四视图_2091918692912287745.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_12

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/krea2+Qwen3.5-自动多风格文生图_2084922609443102721.json、图片生成/文生图/Anima -aesthetic-v1.1-自动提示词动漫文生图（加速版）_2078097784728805377.json、图片生成/文生图/Anima V1.0-超强动漫生成（提示词扩写）_2057810746918133762.json、图片生成/文生图/Krea 2 Text to Image 文生图 (超强写实质感)_2075054887305568258.json、图片生成/文生图/Krea2美人极速版，支持反推。_2092435948138221569.json…）

- **类型**：Text To Image
- **样本数**：24
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 23/24 个有
- `VAEDecode` —— 23/24 个有
- `LoraLoaderModelOnly` —— 22/24 个有
- `CR Prompt Text` —— 21/24 个有
- `ConditioningZeroOut` —— 19/24 个有
- `Fast Groups Bypasser (rgthree)` —— 19/24 个有
- `Label (rgthree)` —— 19/24 个有
- `llama_cpp_parameters` —— 19/24 个有
- `TTResolutionSelector` —— 17/24 个有
- `LoadImage` —— 5/24 个有
- `PreviewImage` —— 3/24 个有
- `SeedVR2LoadDiTModel` —— 3/24 个有
- `SeedVR2LoadVAEModel` —— 3/24 个有
- `SeedVR2VideoUpscaler` —— 3/24 个有
- `ImageScaleToTotalPixels` —— 2/24 个有
- `PrimitiveStringMultiline` —— 2/24 个有
- `ResolutionSelector` —— 2/24 个有
- `INTConstant` —— 1/24 个有
- `Image Comparer (rgthree)` —— 1/24 个有
- `PreviewAny` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1080 | 24 | 71% |
| 高度 | 512 | 512 - 1920 | 24 | 49% |
| 采样步数 | 8 | 8 - 40 | 24 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 24 | 39% |
| 采样算法 | euler | - | 24 | 79% |
| 调度器 | simple | - | 24 | 79% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/24 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1080，24 个样本
- 高度 中位数 512，观测区间 512 - 1920，24 个样本，取值分散，一致性仅 49%
- 采样步数 中位数 8，观测区间 8 - 40，24 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，24 个样本，取值分散，一致性仅 39%
- 采样算法 最常用 euler，24 个样本，一致性 79%
- 调度器 最常用 simple，24 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 高发问题（21/24 个样本）：Steps较低可能导致细节不足
