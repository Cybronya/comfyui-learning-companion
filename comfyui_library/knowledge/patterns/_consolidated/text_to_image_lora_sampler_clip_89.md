---
name: text_to_image_lora_sampler_clip_89
type: Text To Image
frequency: 14
level: strong
coverage: 0.862857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Outpainting图像外绘编辑 自然曝光Lora工作流_2104988768632659969.json, 图片生成/图生图/Qwen Image 2.1一键三视图多表情多视角 角色设定批量产出_2110358998884110338.json, 图片生成/图生图/Qwen Image 2.1一键抠图透明背景 自动识别主体电商产品照_2105356519280824321.json, 图片生成/图生图/Qwen Image 2.1三视图多表情，多视角分镜出图一站搞定_2110844570106945537.json, 图片生成/图生图/Qwen Image 2.1三视图多表情｜多视角人物设定一键出_2110741200184627201.json, 图片生成/图生图/Qwen Image 2.1去除AI感工作流，写实风格人像图生图自然质感提升_2102839671737896962.json, 图片生成/图生图/Qwen Image 2.1去除AI感文生图图生图处理工具_2102540105742372865.json, 图片生成/图生图/Qwen Image 2.1去除AI感｜美少女写实图秒变真实｜告别塑料质感_2102640016362139650.json, 图片生成/图生图/Qwen Image 2.1图像编辑工作流，图生图处理方案_2106515424149065729.json, 图片生成/图生图/Qwen Image 2.1图像编辑工作流，简洁实用的图生图处理方案_2102836660949053442.json, 图片生成/图生图/Qwen Image 2.1图像编辑工作流，简洁实用的图生图处理方案_2106492632359849986.json, 图片生成/图生图/Qwen_Image_2.1去除AI感工作流，写实风格人像图生图自然质感提升_2105864806925430785.json, 图片生成/图生图/Qwen_Image_2.1图像编辑工作流，简洁实用的图生图处理方案_2106169452948709378.json, 图片生成/文生图/Qwen Image 2.1 角色设定集｜多视图表情姿态全包_2112459574203731970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_89

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Outpainting图像外绘编辑 自然曝光Lora工作流_2104988768632659969.json、图片生成/图生图/Qwen Image 2.1一键三视图多表情多视角 角色设定批量产出_2110358998884110338.json、图片生成/图生图/Qwen Image 2.1一键抠图透明背景 自动识别主体电商产品照_2105356519280824321.json、图片生成/图生图/Qwen Image 2.1三视图多表情，多视角分镜出图一站搞定_2110844570106945537.json、图片生成/图生图/Qwen Image 2.1三视图多表情｜多视角人物设定一键出_2110741200184627201.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 13/14 个有
- `ComfySwitchNode` —— 12/14 个有
- `ResolutionSelector` —— 12/14 个有
- `孤海注释` —— 12/14 个有
- `ImageStitch` —— 8/14 个有
- `PreviewImage` —— 4/14 个有
- `PrimitiveBoolean` —— 4/14 个有
- `PrimitiveFloat` —— 4/14 个有
- `EmptyImage` —— 3/14 个有
- `PrimitiveInt` —— 2/14 个有
- `DapaoImagePadDirectionNode` —— 1/14 个有
- `Image Comparer (rgthree)` —— 1/14 个有
- `ImagePadKJ` —— 1/14 个有
- `Textbox` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 14 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 14 | 100% |
| 采样算法 | er_sde | - | 14 | 100% |
| 调度器 | beta | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 80 | 14 | 100% |
| 高度 | 80 | 80 - 80 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，14 个样本，一致性 100%
- 调度器 最常用 beta，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，14 个样本，取值集中（一致性 100%）
- 高发问题（15/14 个样本）：Steps较低可能导致细节不足
