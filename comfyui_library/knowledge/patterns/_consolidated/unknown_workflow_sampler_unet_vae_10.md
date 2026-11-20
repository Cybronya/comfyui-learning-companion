---
name: unknown_workflow_sampler_unet_vae_10
type: Unknown Workflow
frequency: 24
level: strong
coverage: 0.722333
common_nodes: [CLIPLoader, CR Prompt Text, EmptyLatentImage, Image Comparer (rgthree), KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/反推提示词/qwen Image 2.1 全功能工作流_2101887895048114177.json, 图片生成/图生图/Qwen Image 2.1 图像编辑_2104466208149032961.json, 图片生成/图生图/Qwen Image 2.1图像合集_2101928184118861826.json, 图片生成/图生图/Qwen Image 2.1工作流合集_2102019794622042113.json, 图片生成/图生图/Qwen Image 2.1工作流合集_2113788469200908289.json, 图片生成/图生图/Qwen image 2.1多图编辑_2104503241475186689.json, 图片生成/图生图/qwen image2.1AI短剧漫剧人物三视图_2103430511829016578.json, 图片生成/图生图/qwen image2.1产品细节图_2102470856244031490.json, 图片生成/图生图/【Qwen Image 2.1】图像生成 双图版_2102369979093053442.json, 图片生成/图生图/【Qwen Image 2.1】图像生成大合集20步_2102363823524114434.json, 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2102355136613015554.json, 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2112774389644222465.json, 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2113251458060742658.json, 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2114592520796725250.json, 图片生成/图生图/【Qwen Image 2.1】图生图_2102944785588908034.json, 图片生成/图生图/图像生成大合集【Qwen Image 2.1】_2102573883814666241.json, 图片生成/文生图/Qwen Image 2.1工作流合集_2101942307816820738.json, 图片生成/文生图/Qwen image 2.1人物文生图_2112139836655226882.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2101880819102081026.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104545244179165185.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2104558210060480513.json, 图片生成/文生图/【Qwen Image 2.1】图像生成大合集_2108808492491567105.json, 视频生成/图生视频/Qwen_Image_2.1_人物换背景_2107641147056283650.json, 视频生成/图生视频/【Qwen_Image_2.1】图生图_2102955819938705410.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/反推提示词/qwen Image 2.1 全功能工作流_2101887895048114177.json、图片生成/图生图/Qwen Image 2.1 图像编辑_2104466208149032961.json、图片生成/图生图/Qwen Image 2.1图像合集_2101928184118861826.json、图片生成/图生图/Qwen Image 2.1工作流合集_2102019794622042113.json、图片生成/图生图/Qwen Image 2.1工作流合集_2113788469200908289.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 23/24 个有
- `TextGenerateLTX2Prompt` —— 23/24 个有
- `easy setNode` —— 23/24 个有
- `Anything Everywhere3` —— 22/24 个有
- `GetNode` —— 22/24 个有
- `SetNode` —— 22/24 个有
- `ShowText|pysssss` —— 22/24 个有
- `BatchImagesNode` —— 19/24 个有
- `PreviewAny` —— 19/24 个有
- `Fast Groups Bypasser (rgthree)` —— 18/24 个有
- `easy showAnything` —— 18/24 个有
- `Seed (rgthree)` —— 17/24 个有
- `LoraLoaderModelOnly` —— 3/24 个有
- `EmptyImage` —— 2/24 个有
- `JjkText` —— 1/24 个有
- `RepeatLatentBatch` —— 1/24 个有
- `llama_cpp_instruct_adv` —— 1/24 个有
- `llama_cpp_model_loader` —— 1/24 个有
- `llama_cpp_parameters` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 24 | 100% |
| 高度 | 1024 | 1024 - 1024 | 24 | 100% |
| 采样步数 | 40 | 20 - 40 | 24 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | simple | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，24 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，24 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 20 - 40，24 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 simple，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
