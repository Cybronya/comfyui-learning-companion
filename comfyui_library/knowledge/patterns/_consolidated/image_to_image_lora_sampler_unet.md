---
name: image_to_image_lora_sampler_unet
type: Image To Image
frequency: 19
level: strong
coverage: 0.790316
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, RH_LLMAPI_NODE, SaveImage, ShellAgentPluginOutputText, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: [easy boolean, easy float, easy imageScaleDownBy, Latent Input Switch, easy promptLine, LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2030263579697483777.json, 图片生成/图生图/2056637933452615681.json, 图片生成/图生图/2094420053096755202.json, 图片生成/文生图/1981150927354728450.json, 图片生成/文生图/1981208581552988161.json, 图片生成/文生图/1981898675020546049.json, 图片生成/文生图/1984056201858220034.json, 图片生成/文生图/1989169833675730945.json, 图片生成/文生图/【电影效果】人物一致性12分镜 影视剧情分镜制作_2106364207892615170.json, 视频生成/图生视频/2051871461111025665.json, 视频生成/图生视频/2052721515422072834.json, 视频生成/图生视频/1984134656448724993.json, 视频生成/图生视频/1983730005693898754.json, 视频生成/图生视频/1981923431421755394.json, 视频生成/图生视频/1981410642760482818.json, 视频生成/图生视频/1989906208968593410.json, 视频生成/文生视频/Qwen+Next+Scene+影视剧情分镜制作_1983740086821036034.json, 视频生成/文生视频/ai动漫短剧分镜创作llm大模型自动优化ai模型编写提示词分镜九分镜9分镜直出_2011736811663532033.json, 视频生成/文生视频/ai动漫短剧分镜创作llm大模型自动优化ai模型编写提示词分镜九分镜9分镜直出_2012464089221570562.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/2030263579697483777.json、图片生成/图生图/2056637933452615681.json、图片生成/图生图/2094420053096755202.json、图片生成/文生图/1981150927354728450.json、图片生成/文生图/1981208581552988161.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 18/19 个有
- `Int` —— 18/19 个有
- `JjkText` —— 18/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 18/19 个有
- `easy showAnything` —— 18/19 个有
- `PreviewImage` —— 8/19 个有
- `EmptyLatentImage` —— 1/19 个有
- `ImageConcanate` —— 1/19 个有
- `Latent Input Switch` —— 1/19 个有
- `MuyeTextEditOutput` —— 1/19 个有
- `easy boolean` —— 1/19 个有
- `easy float` —— 1/19 个有
- `easy imageScaleDownBy` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | sa_solver | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 600 | - | 1 | 100% |
| 高度 | 800 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy boolean、easy float、easy imageScaleDownBy、Latent Input Switch、easy promptLine
