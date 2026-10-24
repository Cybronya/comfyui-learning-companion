---
name: image_to_image_lora_sampler_unet_42
type: Image To Image
frequency: 12
level: strong
coverage: 0.8475
common_nodes: [CLIPLoader, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen+Next+Scene 风格1致性电影分镜制作_1981989264269418497.json, 图片生成/图生图/Qwen+Next-Scene-V2-一致性电影分镜制作_1984225317587927042.json, 图片生成/图生图/Qwen+Next-Scene-V2-根据主题自动分镜控制_1984212774299516930.json, 图片生成/图生图/Qwen-image-edit 2509 千问剧情分镜制作_1978349545732071426.json, 图片生成/图生图/Qwen-image-edit 2509 千问剧情分镜制作_1981766863715737602.json, 图片生成/图生图/Qwen-next scene（图片反推自动AI自动生词）人物一致自动分镜控制_2005282529886306305.json, 图片生成/图生图/Qwen2509一键电视剧分镜生成_1985607451942834178.json, 图片生成/图生图/Qwen一键电视剧分镜生成_1989357490196369409.json, 图片生成/图生图/Qwen千问一键生成分镜图片+剧情文本（无水印压缩包版）_1985256941666582530.json, 图片生成/图生图/产品一致性多角度工作流_1983860987201818626.json, 图片生成/图生图/广告分镜制作_2013805115051872258.json, 图片生成/图生图/电商版_人物一致自动分镜控制_1989133520150867970.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_42

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen+Next+Scene 风格1致性电影分镜制作_1981989264269418497.json、图片生成/图生图/Qwen+Next-Scene-V2-一致性电影分镜制作_1984225317587927042.json、图片生成/图生图/Qwen+Next-Scene-V2-根据主题自动分镜控制_1984212774299516930.json、图片生成/图生图/Qwen-image-edit 2509 千问剧情分镜制作_1978349545732071426.json、图片生成/图生图/Qwen-image-edit 2509 千问剧情分镜制作_1981766863715737602.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ProcessString` —— 11/12 个有
- `easy promptLine` —— 11/12 个有
- `easy showAnything` —— 11/12 个有
- `RH_LLMAPI_NODE` —— 10/12 个有
- `JjkText` —— 7/12 个有
- `Anything Everywhere3` —— 6/12 个有
- `JoinStringMulti` —— 6/12 个有
- `ShellAgentPluginOutputText` —— 6/12 个有
- `CR Text` —— 5/12 个有
- `ImpactInt` —— 5/12 个有
- `easy convertAnything` —— 5/12 个有
- `GetNode` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `Label (rgthree)` —— 2/12 个有
- `CompressImages` —— 1/12 个有
- `GLM_Vision_ImageToPrompt` —— 1/12 个有
- `ImageListToBatch_` —— 1/12 个有
- `LoadImagesFromURL` —— 1/12 个有
- `MuyeTextEditOutput` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `ShowText` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 12 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | sa_solver | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
