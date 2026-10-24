---
name: image_to_image_lora_sampler_unet_32
type: Image To Image
frequency: 14
level: strong
coverage: 0.855929
common_nodes: [CLIPLoader, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ProcessString, SaveImage, ShellAgentPluginOutputText, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen风格一致性分镜制作工作流｜电影级｜影视剧情｜微电影_2094420053096755202.json, 图片生成/图生图/ai动漫短剧分镜创作 llm大模型自动优化 ai模型编写提示词九分镜直出生图_2055919114291564546.json, 图片生成/图生图/ai动漫短剧分镜创作 llm大模型自动优化 ai模型编写提示词分镜九分镜直出图人物一致性_2056637933452615681.json, 图片生成/图生图/ai动漫短剧分镜创作 llm大模型自动优化 ai模型编写提示词分镜九分镜直出图人物一致性_2075871540650004481.json, 图片生成/图生图/ai动漫短剧分镜创作+llm大模型自动优化+ai模型编写直出图人物一致性_2061692914857766913.json, 图片生成/图生图/ai动漫短剧分镜创作_2062454662489534466.json, 图片生成/图生图/opsv-多角色分镜制作qwenedit_2064636747199369218.json, 图片生成/图生图/qwen edit 2511 IP形象文创衍生品生成_2010188341764956162.json, 图片生成/图生图/qwen edit 2511 广告分镜制作（升级版）  智能多角度多场景生成_1996777809966157826.json, 图片生成/图生图/【Qwen+Next+Scene】镜头风格一致性电影3分镜 影视剧情 电影分镜 制作_1983811786266845185.json, 图片生成/图生图/【产品多角度分镜制作】镜头风格一致性分镜_1985247976631246849.json, 图片生成/图生图/【产品多角度分镜制作】镜头风格一致性分镜_2001863501914226690.json, 图片生成/图生图/【人物写真多角度分镜制作】镜头风格一致性分镜_1998164836343275522.json, 图片生成/图生图/【导演版】AI 短剧分镜生成器——分镜一键生成_1982629374446968834.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_32

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen风格一致性分镜制作工作流｜电影级｜影视剧情｜微电影_2094420053096755202.json、图片生成/图生图/ai动漫短剧分镜创作 llm大模型自动优化 ai模型编写提示词九分镜直出生图_2055919114291564546.json、图片生成/图生图/ai动漫短剧分镜创作 llm大模型自动优化 ai模型编写提示词分镜九分镜直出图人物一致性_2056637933452615681.json、图片生成/图生图/ai动漫短剧分镜创作 llm大模型自动优化 ai模型编写提示词分镜九分镜直出图人物一致性_2075871540650004481.json、图片生成/图生图/ai动漫短剧分镜创作+llm大模型自动优化+ai模型编写直出图人物一致性_2061692914857766913.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `ShellAgentPluginOutputText`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 13/14 个有
- `easy showAnything` —— 13/14 个有
- `JjkText` —— 12/14 个有
- `RH_LLMAPI_NODE` —— 11/14 个有
- `Text Multiline` —— 3/14 个有
- `ttN textOutput` —— 3/14 个有
- `PreviewImage` —— 2/14 个有
- `RH_LLMAPI_Pro_Node` —— 2/14 个有
- `CR Prompt Text` —— 1/14 个有
- `EmptySD3LatentImage` —— 1/14 个有
- `ImageConcanate` —— 1/14 个有
- `LayerUtility: PurgeVRAM` —— 1/14 个有
- `Manual XY Entry Info` —— 1/14 个有
- `MuyeTextEditOutput` —— 1/14 个有
- `RHLLMChatNode` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 14 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | sa_solver | - | 14 | 79% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，14 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，14 个样本，一致性 79%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（14/14 个样本）：Steps较低可能导致细节不足
