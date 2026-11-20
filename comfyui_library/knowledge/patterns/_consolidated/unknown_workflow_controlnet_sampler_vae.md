---
name: unknown_workflow_controlnet_sampler_vae
type: Unknown Workflow
frequency: 38
level: strong
coverage: 0.891342
common_nodes: [AIO_Preprocessor, Control Net Stacker, ControlNetLoader, Efficient Loader, KSampler (Efficient), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, VAEEncode, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/DW姿态+Canny细致线-真人转动漫_1929773564990275585.json, 图片生成/图生图/DW姿态+Depth深度-真人转动漫_1930092106600321026.json, 图片生成/图生图/DW姿态+Tile平铺-真人转动漫_1930094113947860994.json, 图片生成/图生图/DW姿态预处理器-真人转动漫_1929771313303556098.json, 图片生成/图生图/LineArt-线稿转绘3D模型_1932287675519107073.json, 图片生成/图生图/LineArt-线稿转绘剪纸风格_1932292658285150210.json, 图片生成/图生图/LineArt-线稿转绘手绘风_1932293584874012674.json, 图片生成/图生图/LineArt艺术线+DW姿态-品牌及视觉设计_1931196048671178753.json, 图片生成/图生图/LineArt艺术线+DW姿态-真人转3D立体_1931218151722123265.json, 图片生成/图生图/LineArt艺术线+DW姿态-真人转像素画_1931221437401772033.json, 图片生成/图生图/LineArt艺术线+DW姿态-真人转写实二次元_1931197674509545474.json, 图片生成/图生图/LineArt艺术线+DW姿态-真人转动漫_1930088726972547073.json, 图片生成/图生图/LineArt艺术线+DW姿态-真人转卡通插画_1931223197201399810.json, 图片生成/图生图/LineArt艺术线+DW姿态-真人转国漫幻想_1931224560144986114.json, 图片生成/图生图/LineArt艺术线+DW姿态-真人转游戏写实_1931219761273700353.json, 图片生成/图生图/LineArt艺术线+DW姿态-真勾线动漫_1931193606155993089.json, 图片生成/图生图/LineArt艺术线+DW姿态-转2.5D动漫_1930091413541916674.json, 图片生成/图生图/PiDiNet模糊线+DW姿态-真人转动漫_1929791163249889281.json, 图片生成/图生图/SD15+Canny细致线预处理器-真人转漫画勾线彩画风格_1927541486051549185.json, 图片生成/图生图/SD15+HED模糊线预处理器-真人转动漫二次元风格_1929508725713747969.json, 图片生成/图生图/SD15+PiDiNet模糊线预处理器-人物洗图_1929511747064074241.json, 图片生成/图生图/SDXL线稿控制写实摄影_1933378900657643521.json, 图片生成/图生图/SDXL线稿控制动漫游戏二次元插画_1933389632753020930.json, 图片生成/图生图/Scribble涂鸦+DW姿态-真人转动漫_1929794195806961666.json, 图片生成/图生图/Scribble涂鸦预处理器-真人转动漫游戏幻想3D立体_1929516473947996162.json, 图片生成/图生图/open pose姿态预处理器-真人转动漫_1929521877469839362.json, 图片生成/图生图/一张图转绘波普艺术风格_1932678869478772738.json, 图片生成/图生图/一张图转绘肉感动漫_1931192124673601537.json, 图片生成/图生图/一张图转绘肉感动漫_1931596668825698305.json, 图片生成/图生图/两张图转国风_1931952583844540417.json, 图片生成/图生图/两张图转电商风_1931953696156876801.json, 图片生成/图生图/两张图转绘3D盲盒手办_1931611218333597697.json, 图片生成/图生图/两张图转绘刺猬榴莲风_1931611353725730817.json, 图片生成/图生图/两张图转绘家居风_1931955831456071682.json, 图片生成/图生图/两张图转绘日漫二次元_1931957736785772545.json, 图片生成/图生图/两张图转绘猕猴桃画风_1931605466864877570.json, 图片生成/图生图/两张图转绘西瓜画风_1931598015939981313.json, 图片生成/图生图/动漫转绘CG风格_1934863797083676673.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_vae

> 由 `engine/knowledge_consolidation` 从 38 个 workflow 归纳得出（图片生成/图生图/DW姿态+Canny细致线-真人转动漫_1929773564990275585.json、图片生成/图生图/DW姿态+Depth深度-真人转动漫_1930092106600321026.json、图片生成/图生图/DW姿态+Tile平铺-真人转动漫_1930094113947860994.json、图片生成/图生图/DW姿态预处理器-真人转动漫_1929771313303556098.json、图片生成/图生图/LineArt-线稿转绘3D模型_1932287675519107073.json…）

- **类型**：Unknown Workflow
- **样本数**：38
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 38 个 workflow 都包含：
- `AIO_Preprocessor`
- `Control Net Stacker`
- `ControlNetLoader`
- `Efficient Loader`
- `KSampler (Efficient)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEEncode`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 36/38 个有
- `CLIPVisionLoader` —— 15/38 个有
- `IPAdapterAdvanced` —— 15/38 个有
- `IPAdapterModelLoader` —— 15/38 个有
- `AutoNegativePrompt` —— 9/38 个有
- `AILab_ImageStitch` —— 6/38 个有
- `BRIA_RMBG_ModelLoader_Zho` —— 1/38 个有
- `BRIA_RMBG_Zho` —— 1/38 个有
- `SetLatentNoiseMask` —— 1/38 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 38 | 90% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 38 | 100% |
| 采样算法 | dpmpp_2m | - | 38 | 76% |
| 调度器 | karras | - | 38 | 76% |
| 重绘幅度 | 1 | 1 - 1 | 38 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，38 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，38 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，38 个样本，一致性 76%
- 调度器 最常用 karras，38 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 1 - 1，38 个样本，取值集中（一致性 100%）
