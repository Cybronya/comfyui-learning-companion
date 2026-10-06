# LoadImage

## 节点类型

`LoadImage`

## 分类

Image Input

## 作用

从 ComfyUI 的 `input/` 目录制（或上传）一张图片，输出 IMAGE 与可选 MASK。

是图生图 / 反推提示词 / 局部重绘类工作流的入口节点。

## 参数（统计自 404 个真实 workflow，1170 次出现）

| 参数 | 说明 | 实测分布 |
|---|---|---|
| image | 图片文件名 | 多为占位（`None` / `example.png`），分享版工作流不携带真实图 |
| upload | 上传按钮 | 仅 UI 交互，不参与运行 |

## 常见问题与风险

- 分享的 workflow 里 image 通常是占位值，**第一次运行必须手动换成自己的图**，
  否则直接报「file not found」。
- 输出的 MASK 只有图片带 alpha 通道时才有效；需要精确遮罩时应接
  专门的遮罩节点而不是依赖本节点。

## 可信度

Generated（2026-10-06，参数统计实测，行为描述为通行语义）TODO(待验证)
