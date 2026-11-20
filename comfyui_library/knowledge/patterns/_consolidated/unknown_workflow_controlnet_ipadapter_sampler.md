---
name: unknown_workflow_controlnet_ipadapter_sampler
type: Unknown Workflow
frequency: 27
level: strong
coverage: 0.890519
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CR Text Concatenate, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, GetImageSize, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, ImageScale, KSamplerAdvanced, LoadImage, PrepImageForClipVision, PreviewImage, SaveImage, ShowText|pysssss, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/一键室外CAD 彩色平面图_2035278306806861826.json, 图片生成/图生图/一键室外透视效果图_2035281883642208257.json, 图片生成/图生图/不同角度固定风格出图_1946862502572355586.json, 图片生成/图生图/四视图 固定风格出图_2035319023805669378.json, 图片生成/图生图/四视图固定风格出图_1946897613608378369.json, 图片生成/图生图/城市规划转用-模型转效果图_1965249159760629762.json, 图片生成/图生图/多角度 固定风格出图_2035318608062058498.json, 图片生成/图生图/室内白模 一键效果图_2035275301084733441.json, 图片生成/图生图/室内白模一键效果图_1919417360833249281.json, 图片生成/图生图/室外毛坯房 一键转效果图_2035262831423131650.json, 图片生成/图生图/室外毛坯房一键转效果图_1911434727914700801.json, 图片生成/图生图/室外白模 一键效果图_2035272822104268801.json, 图片生成/图生图/室外白模一键效果图_1921200286269112322.json, 图片生成/图生图/室外透视效果图_1915321746482724866.json, 图片生成/图生图/手绘稿 一键效果图_2035248978861756418.json, 图片生成/图生图/手绘稿 毛坯房 一键生成 效果图_2004376302121615361.json, 图片生成/图生图/手绘稿一键效果图_1899564824265707522.json, 图片生成/图生图/手绘稿一键效果图：这个工作流只需要拖入手稿（或者毛坯房照片）和参考图就可以，直接一键生成高质量效果图_2016408567741423618.json, 图片生成/图生图/手绘稿一键效果图：这个工作流只需要拖入手稿（或者毛坯房照片）和参考图就可以，直接一键生成高质量效果图_2054360742618509314.json, 图片生成/图生图/景观效果图一键生成_1998934854655991810.json, 图片生成/图生图/景观照片一键景观效果图_1913988798630326273.json, 图片生成/图生图/景观白模 一键效果图_2035268242247258113.json, 图片生成/图生图/景观白模一键效果图_1921200329788964866.json, 图片生成/图生图/毛坯房 秒出效果图（家装工装通用）_2035256915013406722.json, 图片生成/图生图/毛坯房秒出效果图（家装工装通用）_1908918074056318977.json, 图片生成/图生图/郊区景观照片 秒出景观效果图_2035265199074189314.json, 图片生成/文生图/多角度 固定风格出图_2051966306118848513.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_sampler

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（图片生成/图生图/一键室外CAD 彩色平面图_2035278306806861826.json、图片生成/图生图/一键室外透视效果图_2035281883642208257.json、图片生成/图生图/不同角度固定风格出图_1946862502572355586.json、图片生成/图生图/四视图 固定风格出图_2035319023805669378.json、图片生成/图生图/四视图固定风格出图_1946897613608378369.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 27 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `GetImageSize`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `ImageScale`
- `KSamplerAdvanced`
- `LoadImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `TextInput_` —— 26/27 个有
- `WD14Tagger|pysssss` —— 26/27 个有
- `CR Text` —— 19/27 个有
- `PreviewTextNode` —— 18/27 个有
- `ArgosTranslateTextNode` —— 9/27 个有
- `DeepTranslatorTextNode` —— 7/27 个有
- `Image Comparer (rgthree)` —— 6/27 个有
- `Primitive integer [Crystools]` —— 5/27 个有
- `Note _O` —— 2/27 个有
- `RH_Translator` —— 2/27 个有
- `CLIPVisionLoader` —— 1/27 个有
- `Florence2ModelLoader` —— 1/27 个有
- `Florence2Run` —— 1/27 个有
- `LoraLoaderModelOnly` —— 1/27 个有
- `Seed Everywhere` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | 0.4 - 0.65 | 27 | 89% |
| 采样步数 | randomize | - | 27 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 27 | 100% |
| 采样算法 | 2 | 2 - 3 | 27 | 91% |
| 调度器 | euler_ancestral | - | 27 | 100% |
| 重绘幅度 | sgm_uniform | - | 27 | 100% |
| 宽度 | 512 | 512 - 512 | 27 | 100% |
| 高度 | 512 | 512 - 512 | 27 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.5，观测区间 0.4 - 0.65，27 个样本，取值集中（一致性 89%）
- 采样步数 最常用 randomize，27 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，27 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2，观测区间 2 - 3，27 个样本，取值集中（一致性 91%）
- 调度器 最常用 euler_ancestral，27 个样本，一致性 100%
- 重绘幅度 最常用 sgm_uniform，27 个样本，一致性 100%
- 宽度 中位数 512，观测区间 512 - 512，27 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，27 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
