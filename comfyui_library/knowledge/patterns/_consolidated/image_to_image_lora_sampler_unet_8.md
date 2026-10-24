---
name: image_to_image_lora_sampler_unet_8
type: Image To Image
frequency: 35
level: strong
coverage: 0.831286
common_nodes: [CLIPLoader, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ProcessString, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/(贞贞版)Qwen Edit Next Scene V2模型多镜头分镜制作V1_1980697695679594498.json, 图片生成/图生图/002.Qwen编辑之王023.自动分镜一致性_2034858665345290241.json, 图片生成/图生图/002.Qwen编辑之王025.双主角影视剧情分镜_2034917858714587138.json, 图片生成/图生图/1张图制作影视剧情，支持多分镜制作！！！Qwen模型_1978068040602497025.json, 图片生成/图生图/260110001.超级一致性分镜、短剧分镜神器_2011257263360577538.json, 图片生成/图生图/260110002.双主角影视剧情分镜制作_2011257318050111489.json, 图片生成/图生图/AI-动漫 漫画 短剧 分镜 三视图_2012237563565707265.json, 图片生成/图生图/AI-动漫短剧分镜_2019325060883947522.json, 图片生成/图生图/AI分镜无忧V1.0好用版嘎嘎方便嘎嘎好_2028822578684497921.json, 图片生成/图生图/AI漫剧分镜_2014938088660803585.json, 图片生成/图生图/AI短剧漫剧分镜图（一次性批量生成）_1999501061293473793.json, 图片生成/图生图/AI脚本分镜生成_1986979927847317506.json, 图片生成/图生图/Next+Scene根据参考制作分镜_1995672783566864386.json, 图片生成/图生图/Qwen 2511 next scene V2 电影分镜生成出图一致性影视剧情分镜制作_2008808672310333441.json, 图片生成/图生图/Qwen 2511 next scene V2 电影分镜生成出图一致性影视剧情分镜制作_2016063642785026050.json, 图片生成/图生图/Qwen Edit Next Scene V2模型多镜头分镜制作V1_1980700865378041858.json, 图片生成/图生图/Qwen Edit Next Scene 多镜头分镜制作V1_1979206243426406401.json, 图片生成/图生图/Qwen Next Scene v2 分镜制作_1984092901477154818.json, 图片生成/图生图/Qwen Next Scene 影视剧情分镜制作V1_1980873324416909313.json, 图片生成/图生图/Qwen Next Scene 影视剧情分镜制作V2_1980887759596470274.json, 图片生成/图生图/Qwen Next Scene 影视剧情分镜制作_1983920137306865665.json, 图片生成/图生图/Qwen Next Scene 影视剧情分镜制作一键生成多镜多角度画面人物一致性_2073300067959795713.json, 图片生成/图生图/Qwen Next Scene 影视剧情分镜制作一键生成多镜画面人物一致性_2073291917919608833.json, 图片生成/图生图/Qwen Next Scene 影视剧情分镜制作一键生成多镜画面人物一致性_2101255160981970946.json, 图片生成/图生图/Qwen Next Scene 影视剧情分镜制作一键生成多镜画面人物一致性_2101289147616030721.json, 图片生成/图生图/Qwen ——影视剧情分镜制作（ai短剧）_1980273658113515522.json, 图片生成/图生图/Qwen+Next+Scene 分镜头  角色一致性_2039660310126137345.json, 图片生成/图生图/Qwen+Next+Scene 分镜头生成 角色一致性_2037092197958422529.json, 图片生成/图生图/Qwen+Next+Scene 分镜生成出图一致性影视剧情分镜制作_2060714698395447298.json, 图片生成/图生图/Qwen+Next+Scene 影视剧情分镜制作_2062812796873691138.json, 图片生成/图生图/Qwen+Next+Scene 影视剧情分镜制作_sfw_2015416285655474178.json, 图片生成/图生图/Qwen+Next+Scene 影视剧情分镜制作_本地编码_2015264925316292610.json, 图片生成/图生图/Qwen2509影片分镜头剧情_1981664964194770946.json, 图片生成/图生图/QwenNextScene短视频12分镜图_1982228139298439169.json, 图片生成/图生图/Qwen影视剧情分镜制作_2015305786242633730.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_8

> 由 `engine/knowledge_consolidation` 从 35 个 workflow 归纳得出（图片生成/图生图/(贞贞版)Qwen Edit Next Scene V2模型多镜头分镜制作V1_1980697695679594498.json、图片生成/图生图/002.Qwen编辑之王023.自动分镜一致性_2034858665345290241.json、图片生成/图生图/002.Qwen编辑之王025.双主角影视剧情分镜_2034917858714587138.json、图片生成/图生图/1张图制作影视剧情，支持多分镜制作！！！Qwen模型_1978068040602497025.json、图片生成/图生图/260110001.超级一致性分镜、短剧分镜神器_2011257263360577538.json…）

- **类型**：Image To Image
- **样本数**：35
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 35 个 workflow 都包含：
- `CLIPLoader`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `Int` —— 34/35 个有
- `easy showAnything` —— 34/35 个有
- `RH_LLMAPI_NODE` —— 33/35 个有
- `ShellAgentPluginOutputText` —— 30/35 个有
- `Anything Everywhere3` —— 26/35 个有
- `PreviewImage` —— 8/35 个有
- `Anything Everywhere` —— 4/35 个有
- `CR Prompt Text` —— 3/35 个有
- `CheckpointLoaderSimple` —— 3/35 个有
- `Text Concatenate` —— 3/35 个有
- `CFGNorm` —— 2/35 个有
- `Comfly_LLm_API` —— 2/35 个有
- `ModelSamplingAuraFlow` —— 2/35 个有
- `easy imageConcat` —— 2/35 个有
- `DuckHideNode` —— 1/35 个有
- `LayerUtility: ImageChannelMerge` —— 1/35 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 35 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 35 | 100% |
| 采样算法 | sa_solver | - | 35 | 91% |
| 调度器 | simple | - | 35 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 35 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 35/35 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，35 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，35 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，35 个样本，一致性 91%
- 调度器 最常用 simple，35 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，35 个样本，取值集中（一致性 100%）
- 高发问题（35/35 个样本）：Steps较低可能导致细节不足
