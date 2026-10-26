---
name: text_to_image_lora_sampler_clip
type: Text To Image
frequency: 98
level: strong
coverage: 0.908786
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/开源版图生视频Q版萌系｜MiniMax H3文生视频图片转视频_2095000997281226753.json, 图片生成/文生图/开源版电商图生视频｜MiniMax H3文生视频图片转视频_2098232921382543362.json, 视频生成/图生视频/FL2VA开源图生视频｜MiniMax H3视频运镜人物特效_2092753761356832770.json, 视频生成/图生视频/FL2VA开源方案 MiniMax H3图生视频人物特效运镜_2104315661873934337.json, 视频生成/图生视频/FL2VA开源版图生视频 MiniMax H3 视频运镜生成_2094246618005590018.json, 视频生成/图生视频/FL2VA开源版图生视频，视频运镜人物特效随心控_2110878802493657089.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3 人物特效运镜稳_2096237643783823361.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3 视频运镜流畅人物特效在线_2105504355377041409.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3人物特效视频运镜_2089497492621717505.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3人物特效视频运镜_2091005039648268290.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3人物运镜特效_2090595072525029377.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3人物运镜特效_2090914518158368769.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3扩图人物特效_2092734556272152578.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3视频生成工作流_2094800003058458625.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3视频运镜人物特效_2092029507527077890.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3视频运镜人物特效_2095848877701287937.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3视频运镜生成_2094592355511922689.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3视频运镜生成_2095095190884282369.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3运镜人物特效_2093460752253411329.json, 视频生成/图生视频/FL2VA开源版图生视频｜MiniMax H3运镜特效生成_2095949959383314433.json, 视频生成/图生视频/FL2VA开源版视频运镜｜MiniMax H3图生视频特效_2101211987798740993.json, 视频生成/图生视频/FL2VA开源版首帧单图生视频｜MiniMax H3人物特效直出_2091642698561310721.json, 视频生成/图生视频/FL2VA开源版首帧参考生视频｜MiniMax H3图生视频_2092071846270296065.json, 视频生成/图生视频/FL2VA开源版高质量图生视频｜MiniMax H3特效版_2095968043171147778.json, 视频生成/图生视频/FL2VA开源版｜MiniMax H3图生视频人物特效直出_2090918607361499138.json, 视频生成/图生视频/FL2VA开源版｜MiniMax H3图生视频人物特效运镜_2089800258913132546.json, 视频生成/图生视频/FL2VA开源首帧生视频｜MiniMax H3单图直出_2091805062271164418.json, 视频生成/图生视频/FL2VA首尾帧扩写视频｜MiniMax H3图生视频直出_2091269321677950978.json, 视频生成/图生视频/H3 FL2VA开源版图生视频 创意视频生成工具_2099598984766644225.json, 视频生成/图生视频/H3 FL2VA开源版图生视频 创意视频生成工具_2099902148627750913.json, 视频生成/图生视频/H3 FL2VA开源版图生视频 创意视频生成工具_2100662619723096066.json, 视频生成/图生视频/H3 FL2VA开源版图生视频 脑洞创意电影感视频生成_2099575018731696129.json, 视频生成/图生视频/H3图生视频RH版首帧驱动 视频生成处理工具_2100680247116132353.json, 视频生成/图生视频/MiniMax H3 FL2VA图生视频开源版｜运镜场景特效升级_2108407586692362241.json, 视频生成/图生视频/MiniMax H3 FL2VA图生视频｜开源版运镜人物特效出片_2108447113444159490.json, 视频生成/图生视频/MiniMax H3 FL2VA图生视频｜视频运镜人物特效 开源版自由可控_2104075142203789313.json, 视频生成/图生视频/MiniMax H3 FL2VA开源图生视频人物特效运镜生成_2088255083204141057.json, 视频生成/图生视频/MiniMax H3 FL2VA开源图生视频，人物特效运镜自选_2110476837511065601.json, 视频生成/图生视频/MiniMax H3 FL2VA开源图生视频｜运镜丝滑人物特效惊艳_2103742224029802497.json, 视频生成/图生视频/MiniMax H3 FL2VA开源图生视频｜零成本上手视频创作_2113560533579423745.json, 视频生成/图生视频/MiniMax H3 FL2VA开源图生视频｜高质量视频生成_2094585368157974530.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 上传图片直出视频处理工具_2113421902302769153.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 人物特效运镜图生视频工具_2113769554110406658.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 场景特效运镜图生视频工具_2113055300109553666.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版 场景特效运镜图生视频工具_2114108324567408642.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-图生视频-运镜特效版｜人物类特效直出_2114284451885830146.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版-图生视频｜人物特效运镜自由_2114181687352586241.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版人物图生视频｜场景运镜特效_2108454787669913602.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频 人物特效运镜_2098303984741208065.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频 首尾帧控制视频生成_2105077087165042689.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频人物特效视频运镜_2088248855371542529.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频工作流，人物类特效视频运镜图生视频方案_2107604019341516802.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频工作流，人物类特效视频运镜图生视频方案_2108435791927144450.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频，人物特效视频运镜图生视频方案_2103957365132447745.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频，人物类特效运镜控制灵活_2114483007494123521.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频，首尾帧驱动运镜自然动作流畅_2114447271457812481.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜人物特效生成_2094934422737997826.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜人物特效视频运镜_2097975771343183873.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜人物特效视频运镜轻松驾驭_2114282717230751746.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜人物特效运镜流_2114032174163914754.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜人物特效运镜自由_2110712117195264001.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜人物运镜高质量生成_2097120793103781889.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜免费开源视频生成首选_2113548233401257986.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜场景特效视频运镜_2114024342660149250.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜场景特效运镜加持_2108399643406200834.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜画面稳定运镜高级_2108078757767639042.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜视频运镜特效生成_2094918652628914178.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜角色表演人物特效_2114064141907480578.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜运镜丝滑人物特效_2108065044322938882.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜运镜丝滑人物特效，免费用_2107324332400791553.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版图生视频｜运镜特效_2095596241626423297.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版首尾帧参考生视频_2098853156762509313.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜人物图生视频运镜自然_2108075742809645058.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜人物特效图生视频运镜流畅_2108425587789484033.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜人物特效运镜视频生成_2095967424469364738.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜图生视频人物特效运镜_2094925777950306306.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜图生视频免费白嫖就用它_2101521476091465729.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜图生视频带运镜 人物特效在线_2097570331480383490.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜图生视频带运镜人物特效_2103108865687646209.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜图生视频视频运镜 人物类特效加持_2104062765215342593.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜图生视频运镜特效_2095582459734876161.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜图生视频运镜特效工作流_2094938564432842753.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜图生视频运镜生成_2094904171962134530.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜图生视频运镜生成_2095956309467287554.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜视频运镜人物特效图生视频_2097510178395615233.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜视频运镜图生视频特效_2101239883649085441.json, 视频生成/图生视频/MiniMax H3 FL2VA开源版｜角色一致性图生视频生成_2097492746364870657.json, 视频生成/图生视频/MiniMax H3 FL2VA视频运镜方案，人物类特效图生视频_2110882143445540866.json, 视频生成/图生视频/MiniMax H3图生视频开源FL2VA 参考图直出动态运镜_2104318849544974337.json, 视频生成/图生视频/MiniMax H3图生视频｜高质量视频生成工作流_2094935914660323330.json, 视频生成/图生视频/MiniMax H3开源图生视频｜FL2VA人物特效运镜生成工作流_2097458572249624578.json, 视频生成/图生视频/MiniMax-H3图生视频RH版首帧驱动｜单图起手直出视频，动起来更自然_2100452638570663938.json, 视频生成/图生视频/MiniMaxH3FL2VA图生视频开源版ENGENGENG_2087148465603301378.json, 视频生成/图生视频/MiniMaxH3开源版图生视频ENGENG_2087138788249264130.json, 视频生成/图生视频/MiniMaxH3首帧生视频图生视频_2087405631845261314.json, 视频生成/图生视频/MiniMax_H3_FL2VA开源图生视频，人物特效运镜自选_2113106296496017409.json, 视频生成/图生视频/Minimax H3首尾帧自动提示词-转场场景特效图生视频_2087362211432976385.json, 视频生成/图生视频/中文提示词首尾帧参考生视频MiniMax H3图生视频可调时长_2088385544035328001.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip

> 由 `engine/knowledge_consolidation` 从 98 个 workflow 归纳得出（图片生成/文生图/开源版图生视频Q版萌系｜MiniMax H3文生视频图片转视频_2095000997281226753.json、图片生成/文生图/开源版电商图生视频｜MiniMax H3文生视频图片转视频_2098232921382543362.json、视频生成/图生视频/FL2VA开源图生视频｜MiniMax H3视频运镜人物特效_2092753761356832770.json、视频生成/图生视频/FL2VA开源方案 MiniMax H3图生视频人物特效运镜_2104315661873934337.json、视频生成/图生视频/FL2VA开源版图生视频 MiniMax H3 视频运镜生成_2094246618005590018.json…）

- **类型**：Text To Image
- **样本数**：98
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 98 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3FL2VAEncode`
- `RHMiniMaxH3FL2VAFirstFrameCondition`
- `RHMiniMaxH3FL2VAModelLoader`
- `RHMiniMaxH3FL2VATarget`
- `RHMiniMaxH3FL2VATextEncoderLoader`
- `RHMiniMaxH3FL2VAVAELoader`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 94/98 个有
- `ImageResize+` —— 91/98 个有
- `SaveImage` —— 27/98 个有
- `Int` —— 16/98 个有
- `PreviewImage` —— 8/98 个有
- `ImpactSwitch` —— 7/98 个有
- `CR Text` —— 6/98 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/98 个有
- `EmptyImage` —— 4/98 个有
- `PrimitiveInt` —— 4/98 个有
- `intToFloat _O` —— 4/98 个有
- `ImageResizeKJv2` —— 2/98 个有
- `DF_Int_to_Float` —— 1/98 个有
- `GetImageSize` —— 1/98 个有
- `GetNode` —— 1/98 个有
- `RHHiddenNodes` —— 1/98 个有
- `RHMiniMaxH3FL2VALastFrameCondition` —— 1/98 个有
- `RH_LLMAPI_Pro_Node` —— 1/98 个有
- `RH_OneShot_Prompter` —— 1/98 个有
- `SetNode` —— 1/98 个有
- `ShowAnything|Mie` —— 1/98 个有
- `easy anythingIndexSwitch` —— 1/98 个有
- `easy int` —— 1/98 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 98 | 100% |
| 高度 | 80 | 80 - 80 | 98 | 100% |
| 采样步数 | 4 | 4 - 4 | 98 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 98 | 100% |
| 采样算法 | er_sde | - | 98 | 100% |
| 调度器 | beta | - | 98 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 98 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 99/98 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，98 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，98 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，98 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，98 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，98 个样本，一致性 100%
- 调度器 最常用 beta，98 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，98 个样本，取值集中（一致性 100%）
- 高发问题（99/98 个样本）：Steps较低可能导致细节不足
